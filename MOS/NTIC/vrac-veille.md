~15 minutes d'exposé, le vendredi 23 de 11:55 à 12:10.

> _Les présentations des premières semaines pourraient être focalisées sur le contexte, axes de recherche ainsi que la méthodologie et outils de veille._

## Pts de comparaison

- [x] Memory-safe ou pas
- [x] Gestion de la mémoire
- [x] Abstractions
- [x] LLVM
- [x] C ABI
- [x] Interop avec le C
- [x] Ambitieux
- [x] Maturité / date de création
- [x] écosystème
- [x] tollchain
- [x] Traitement des erreurs

Tous essaient de garder la puissance du C tout en modernisant la DX, avec des mécanismes de safety par défaut, ms de manières radicalement différentes.

### Gestion de la mémoire

- Memory-safe ou pas
- Gestion de la mémoire
- Abstractions

Comme C, Zig et C3 ne sont pas garbage-collected : c possible de faire des use after free, d'avoir des dangling pointers, de sortir des limites d'un tableau, etc.
Rust n'est pas garbage-collected non plus, ms a ce système du borrow checker : le compilateur s'assure des références "empruntées" pour interdire les fameux bugs qu'y a en C.

Go et les langages interprétés sont garbade-collected : la collection des déchets c intrinsèquement non-déterministe, donc dans des environnements embarqués ou avec d'autres fortes contraintes, c juste pas envisageable.

Bref : avec le C on a un langage puissant, fais ce que tu veux, donc c à nous le développeur de rattraper ces problèmes.

Le truc : si on considère le nouveau dév, qui essaie de se mettre au bas-niveau, d'apprendre un nouveau langage, ms veut pas apprendre Rust car trop dur, ni C car pas memory-safe -> c là que Zig se place très bien, pr rendre abordable le travail bas-niveau et sans cacher les ce que ça coûte.

> Zig [...] how minimal it feels - you can comfortably go through the language documentation in a couple hours because there just isn't that much to learn.
> Zig comfortably gets so much done with comparably so few features.

En Zig, y a pas d'allocation cachée : toutes les allocations sont uniquement celles qu'on demande à Zig de faire, le langage n'en fait aucune pour nous -> le contrôle de l'allocation de mémoire est on ne peut plus explicite (`ArrayList(i32).init(...)` et `...` ça peut être un page_allocator, un c_allocator, un FixedBufferAllocator, etc).
Zig a le keyword `defer` qui, à la compilation, décale la ligne à la fin du bloc (et run au moment où le scope du bloc est sur le point d'être franchi) : qd on alloue une page mémoire, la ligne d'après c un defer de libérer cette mémoire, comme ça à la lecture on voit immédiatement que la mémoire est bien libérée (l'alloc et le free sont proches dans le code), et à la compilation c'est mis au bon endroit.

En Zig, y a une interface unifiée et cohérente pr la gestion de la mémoire, les allocators peuvent facilement être remplacés ds le code pr viser différentes archs (y compris le wasm et du bare metal).

Ce caractère explicite est pratique jusqu'à des environnements embarqués, car en lisant le code on sait quasiment ce qui va prendre du temps ou non.

La performance : la compilation de Rust avec le Borrow Checker, ça rend l'exécution + lourde (tous les voitures n'ont pas besoin d'être construites comme des tanks).

Rappel de C :

```c
char* memoire = malloc(128); // allouer
memset(memoire, 0, 128); // utiliser
free(memoire); // libérer
```

Equivalent en Zig :

```zig
var memoire = try allocator.alloc(u8, 128); // allouer
defer allocator.free(memoire);; //liberer
for (memoire) |*octet| { // utiliser
    octet.* = 0;
}
```

### Interop

- LLVM
- C ABI
- Interop avec le C

L'intégration de C en Zig a l'air juste légendaire...
En fait c la meilleure toolchain pour C.
Cross-compilation vers C/C++ supportée nativement.
En fait Zig a été conçu avec l'interop C en tête, et traite le C comme un _first-class citizen_ (y a vrmt pas d'équivalent en français) donc y a un feeling que les imports C sont natifs : on peu importer des headers C et utiliser les fonctions comme si c'était du Zig :

```zig
const std: type = @import("std");
const c: type = @cImport({
    @cInclude("ctype.h");
});

pub fn main() !void {
    const truc: c_int = c.isdigit('8');
}
```

Ca veut dire qu'on peut porter progressivement une codebase C vers du Zig, en important des fonctions C toutes prêtes !

Aussi, Zig vient avec un compilateur de C/C++ qui est de très loin le + facile et rapide et à installer sous Windows (j'ai Visual Studio, GCC, je sais de quoi je parle).
En fait Zig c pas juste un langage, c aussi une toolchain, qui veut unifier tt ça ds un système cohérent.

En Rust y a toute une cérémonie, avec des labels `extern` et `unsafe`, des frontières minutieusement définies :

```rs
extern "C" fn cmp_i32(a: *const c_void; b: *const c_void) -> c_int { // -1, 0 ou 1
    let pa = unsafe { &*(a as *const i32) };
    let pb = unsafe { &*(b as *const i32) };
    (*pa).cmp(pb) as c_int
}
```

En Zig, y a un mot-clef `comptime` qui exécute du code à la compilation et pas à l'exécution (je trouve ça analogue au Server-Side Rendering en Next.js) : fini les macros du C (et + généralement le pre-processing ie. l'étape n°1/4 de la compilation de C avec GCC).

```
comptime {
    var i = 0;
    while (i < 100) : (i +=1) { ... }
}
```

[comparer à l'assembleur généré]

Zig et Rust ont en fait la mm stratégie pr les types génériques : le compilateur regarde quels types font vraiment être passés à la fonction et créé une fonction dédiée pour chaque type :

```
fn max(comptime T: type, a: T, b: T) T {
    return if (a > b) a else b;
}

fn maxfloat(a: f32, b: f32) f32 {
    return max(f32, a, b);
}
fn maxint(a: u64, b: u64) u64 {
    return max(u64, a, b);
}
```

Fini l'usage de LLVM en Zig (je crois qu'on se rend pas compte d'à quel pt c ambitieux)

La correspondance entre du code Rust et les instructions mémoires et le timing est moins évidente qu'avec Zig ou C, qui sont "+ proches du métal".
C'est une question de prédictabilité.

LLVM c la façon "moderne" et class-platform : on compile pas en binaire de chaque arch, ms vers une représentation intermédiaire qi s'appelle LLVM IR (oui, Intermediate Representation, le nom est bien choisi), et LLVM est un back-end qui se charge d'optimiser tout ça et de compiler vers pour les archs de ce qu'on veut.

Rust utilise LLVM pr la codegen. Zig peut l'utiliser aussi ms utilise par défaut... son propre back-end (ils font vraiment tout)

### Maturité

- Maturité / date de création
- écosystème
- toolchain
- ambitieux (révolution vs amélioration)

Le C a une stdlib très mature.

En Zig, c pas aussi mature que Rust, ms ça s'améliore à grande vitesse :

- Les erreurs de compilation sont particulièrement explicites.
- Y a un framework de test qui est natif (comme pytest en Python).
- On peut choisir de compiler en optimisant au choix la safety, la petitesse du binary qui sort, ou la vitesse.
- Le langage se veut minimal, et juste simple à prendre en main (comme C, + ou -).
- La toolchain pr build (targets, étapes, linker, tests, etc), c pas des dingueries genre Make/CMake/Premake, mais du **code**, en Zig lui-mm, en code sur lequel on peut raisonner !
  Ca assure la répétabilité.

En Rust :

- Cargo, le package manager qui manage l'écosystème de crates, et c vrmt mature, complet, y a de tout, comme en Python.
- En toolchain y a déjà de quoi faire bcp : intégration ds les éditeurs de texte, framework de tests, doc, cross-compilation, etc

C3 se veut comme une petite amélioration, les autres comme une révolution.
C3 essaie autant que possible de ressembler au C, de donner une sensation similaire au C, juste amélioré : syntaxe + propre, qlq garde-fous, prédictabilité, et une toolchain moderne.
Zig cherche pas à améliorer le C ms à l'englober, le compiler, bref le remplacer.
C'est bcp + ambitieux.

### Syntaxe

- Traitement des erreurs

```zig
const std = @import("std");

pub fn main() !void {
    var a: []u8 = "Truc";
    const b = 42;
    const Truc = struct {
        field1: []const u8,
        field2: u8,
    };
    const truc = Truc{
        .field1 = "machin",
        .field2 = 128,
    };
    var allocator = std.heap.page_allocator;
    var ls = std.ArrayList(i32).init(allocator);
    defer ls.deinit();
    try ls.append(10)
    return;
}
```

En Zig, les erreurs sont des valeurs : y a pas de control flow caché derrière des Exception qui se propage chèpakoi, ce sont des valeurs ordinaires, fortement typées.
Soit on a une valeur, ou un nom d'erreur, ou choisit de propager ou gérer l'erreur.
A nouveau c très explicite, on est obligés de gérer tous les erreurs qu'on peut avoir.
Le langage nous mène vers un code clair plutôt que vers un truc malin ms alembiqué.

En Rust, la gestion des erreurs c explicite aussi, ms Rust encourage l'usage de types + "riches", le code reste compact sans perdre en clarté.

```
const std = @import("std");
const allocator = std.heap.page_allocator;

pub fn openfile(path: []u8) std.fs.File.OpenError!std.fs.File {
    return std.fs.cwd().openFile(path, .{
        .mode = .read_only,
    })
}

pub fn main() !void {
    const argv = std.process.argsAlloc(allocator) catch |e| {
        ...
        return;
    }
    defer std.process.argsFree(allocator, argv);
    if (argv.len == 1) {
        ...
        return;
    }

    // blabla


    const filepath = argv[1]
    const f = openfile(filepath) catch |e| switch (e) {
        error.FileNotFound => {
            ...
        },
        else => {
            ...
        }
    }
    const buf = try allocator.alloc(u8, 42)
    _ = try f.read(buf);
    return;
}
```

```zig
const std = @import("std");

pub fn main() !void {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile(
        "truc.txt",
        .{ .mode: .read_only }
    );
    defer file.close();

    const contents = try file.readToEndAlloc(allocator, std.math.maxInt(usize));
    defer allocator.free(contents);

    std.debug.print("Contenu du fichier : {s}\n", .{contents});
}
```

Le type de retour c `std.fs.File.OpenError!std.fs.File`, à droite du `!` c le type qd c bon, à gauche c le type qd c une erreur.
Qd on appelle la fn, on traite direct le cas où y a une erreur (`catch |e|`) avant mm d'assigner à une variable la potentielle bonne valeur : ça nous force à gérer chaque possibilité d'erreur.

Sans être memory-safe au sens de la garbage collection ou au sens de Rust, y a des features de ce langage qui s'en rapprochent et permettent d'éviter un tas de bugs simples.
La compilation peut crash, un peu comme en Rust, si on essaie d'accéder au-delà de la mémoier allouée ; c bcp + safe comme ça qu'en C avec des undefined behavior qui préviennent pas (et pardonnent pas).
Et les erreurs de compilation se veulent claires, pas un vieux segfault.

En Rust, on renvoie un Enum pour renvoyer un Ok ou un Error, et on fait du `match` dessus.

En Zig, y a pas de surcharge d'opérateur.

En Zig, le `if` est une expression, qui renvoie une valeur, je trouve ça génial ça retire le besoin d'une syntaxe ternaire séparée :

```zig
const std: type = @import("std");
const E: type = error{NaN};

fn toInt(ch: u8) E!u8 {
    return if (ch >= '0' and ch <= '9') ch - '0' else E.NaN;
}
```

```rs
// pub fn openfile(path: []u8) std.fs.File.OpenError!std.fs.File {
//     return std.fs.cwd().openFile(path, .{
//         .mode = .read_only,
//     })
// }
use std::{
    error::Error,
    fs
}

fn openfile() -> <Result, Box<dyn Error>> {
    let text = fs::read_to_string("path.txt")?;
    let n: u32 = text.trim().parse()?;
    Ok(n)
}
```

Rust n'essaie pas d'être transparent mais safe par défaut, et le compilateur sert de garde du corps qui va bloquer un certain nbr "d'anti-patterns".
Au début on se "bat" contre, c d'abord un prof puis un allié.

Rust c une épée à double-tranchant.

Y a une qté aberrante d'abstractions (itérateurs, pattern matching, enums) on se croirait ds un langage très haut-niveau voire paradigme fonctionnel :

```rs
fn sum_squares(nums: &[i32]) -> i32 {
    nums.iter().copied().map(|n| n * n).sum()
}

fn main() {
    let vec = [3, 4, 12];
    println!("{}", sum_squares(&vec));
}
```

Et on fait confiance au compilateur et ses optimisations pr que le binaire généré soit efficace.
Ms c exactitude d'abord et perf ensuite.

Interop avec du C et usage de pointeurs en unsafe

```rs
extern "C" { fn sqrtf(x: f32) -> f32; }

fn troisieme_octet(bug: &mut[u8, 4]) {
    unsafe {
        let p = buf.as_mut_ptr().add(2);
        *p = 42;
    }
}
```

La zone de danger est délimitée explicitement.

Le compilateur de Rust veut tout monomorphiser, tout le code a l'air de se ressembler.

C3 se définit comme un petit langage, proche du C, qui n'essaie pas de réinventer la roue :

- ça garde cque les gens apprécie en C (prédictabilité, la stabilité de l'ABI, la proximité avec les instructions mémoire),
- et ça offre une toolchain + moderne : une vraie notion de modules.

C3 utilise des optionals :

```c3
int? a = 1;
int? b = io::FILE_NOT_FOUND?;
```

Y a le mot-clef `defer` comme en Zig.
Par rapport au C, ça ajoute aussi des types génériques, des slices, un meilleur type-checking, et du zero-init (les variables valent 0 par défaut à l'initialisation au lieu d'être undefined).
Y a un `fn` devant les fonctions :

```c
int add(int *a, int *b) {
    return *a + *b;
}
```

```c3
fn int add(int* a, int* b) {
    return *a + *b;
}
```

Comme avec Zig, on peut appeler du C depuis C3, et là c encore plus trivial à faire :

```c3
extern fn int puts(char*);
```

## Pts spécifiques

- Quels projets / types de projets existent ds tel langage ?

- Rust rend difficile l'écriture de mauvais code ; Zig rend facile l'écriture de bon code.

    > Rust philosophy: make it hard to write bad code
    > Zig philosophy: make it easy to write good code

- Zig est en 0.truc : rappeler qu'en SemVer ça fait que truc est la majeure, ça veut dire instable donc permis de faire des breaking changes à chaque majeure, et Zig en profite (cf. la dernière release).
  Conséquence : des tutos datant d'octobre sont déjà obsolètes.
  On a déjà vu des langages se tirer une balle ds le pied en allant trop vite vers le 1.0 puis être coincé ds l'obligation d'être rétrocompatible.

- C n'est pas memory-safe, Rust est trop dur ; Zig arrive pile au bon endroit.
- Rust c qd on veut du long-terme, maintenable, qui supporte l'exactitude mm en concu.
- Zig : code transparent, minimum d'abstractions, allocations mémoire explicites, chemin prévisible.
  On choisit Zig si on veut importer du C direct, contrôler les allocations -> kernel, bootloader et autres firmware où le déterministe est non-négociable
- Rust : invariance qui tient mm qd on scale up.
  On choisit Rust si on fait un service complexe, avec de la concu, long-terme, et que l'exactitude c non-négociable -> stockage, db, communications réseau, compilateurs, et là où y a bcp de concu

## Bibligraphie (Rust Zig C3)

- Sites web des langages
    - https://rust-lang.org/
    - https://ziglang.org/
    - https://c3-lang.org/
- Release notes / changelog
    - https://blog.rust-lang.org/2025/12/11/Rust-1.92.0/
    - https://ziglang.org/download/0.15.1/release-notes.html
    - https://c3-lang.org/blog/
- Code source
    - https://github.com/rust-lang/rust
    - https://codeberg.org/ziglang/zig
        - [zig#16270 - make the main zig executable no longer depend on LLVM, LLD, and Clang libraries](https://github.com/ziglang/zig/issues/16270)
    - https://github.com/c3lang/c3c
- Comparaisons
    - https://c3-lang.org/faq/compare-languages/
    - https://ziglang.org/learn/why_zig_rust_d_cpp/
- YT
    - Low Level
        - [zig will change programming forever](https://www.youtube.com/watch?v=pnnx1bkFXng)
    - Fireship
        - []()
    - TheTechyShop
        - [Zig vs Rust: Who’s Closer to the Metal?](https://www.youtube.com/watch?v=ftDTHtgPKJo)
        - [C3 vs Zig in 2025: Who’s Really Fixing C?](https://www.youtube.com/watch?v=y3tDZACGRAY)

## Vrac autres

Zig is definitely an amazing language, but there is so much you should have mentioned, maybe in another video, because as a C developer, Zig is really everything I wish C was.

1 - It's simple and easy to use.
2 - I'ts the most refactorable language (meaning you don't have to jump in 30 files fixing headers and function prototypes.
3 - Comptime is capturing 90% of the power of C++ templates/Macros, while still being very readable and type safe.
4 - The build system is insanely good, I replaced make/cmake with Zig, and with Zig itself it's really amazing.
5 - Zig found the right balance of freedom, meaning you can do exactly what you are doing in C (aka crazy casting and weird stuff unlike Rust) but at the same time the language design makes it very inconvenient and verbose to do so. Which makes it actually easier to just to the right thing and not take any shortcuts. So for once the Type system is actually one that doesn't deceive you because of how loose it is like C or how tight it is like Rust.
6 - Allocators are first class citizen. Even the Std is build around that which is amazing. I really don't get how a manual memory managed language like C didn't come with some form of interface for allocators.
7 - The interops with C is the most natural, intuitive, and straightforward that I've ever seen. You literally just add an @cImport("header.h"); and a exe.addCsourceFile("") in your build.zig and you are good to go.
8 - Zig also has integrated unit testing, which makes it so easier and cheaper to test code. In C I would literally spend 30 minutes writing some code and one hour testing it properly. In Zig you write a function write 2/3 tests forget about it and just do a quick zig build test and you are good to go. Which is also why it's so easy to refactor Zig btw.
9 - No hidden memory allocation, no hidden control flow, everything you read is everything you get, you don't have to guess whether this functions aborts, returns -1 or 0, or whether it sets ernno.
10 - The error handling and all the builting safety features makes it so much easier to write fast and correct code.

I could go on an on but TLDR if you are a C developer you should definitely try Zig as I'm sure it's going to be the real C replacement. In System level programming.

---

Let's all agree on the fact that Zig has by far the best build system. It is literally built into the language itself. No more bullshit Makefiles, pkgconf or Ninja. Don't even get me started with CMake.

---

writing in rust feels like: here’s a set list of the most ideal ways to write code, proven over the last few decades, and we want you to write in this way specifically, no other way. for that reason, I’d say zig is closer to the metal, but I like rust more :3

---

If I am rewriting C code, I choose zig.
If I am rewriting python code, I choose rust.
Zig offers safety without sacrificing the performance.
Rust offers performance without sacrificing the abstractions.

---

Once zig hits 1.0 it will gain a lot of followers
