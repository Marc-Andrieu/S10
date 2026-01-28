#include <vector>
#include <iostream>
#include <fstream>
using namespace std;

class Vertex {
    public:
        double x;
        double y;
        double z;
        int indice_face;
        Vertex() : x(0), y(0), z(0), indice_face(0) {}
        Vertex(double x_, double y_, double z_, int indice_face_) 
            : x(x_), y(y_), z(z_), indice_face(indice_face_) {}
        void set(double x_, double y_, double z_) {
            x = x_;
            y = y_;
            z = z_;
        }
};

class Triangle {
    public:
        vector<int> indice_sommets = {0, 0, 0};
        vector<int> indice_faces = {0, 0, 0};

        Triangle() : indice_sommets({0, 0, 0}), indice_faces({0, 0, 0}) {}
        Triangle(vector<int> sommets, vector<int> faces) 
            : indice_sommets(sommets), indice_faces(faces) {}

        int return_face(int sommet) {
            return indice_faces[(sommet + 1) % 3];
        };
};

class Mesh{
    public:
        vector<Vertex> tabV;
        vector<Triangle> tabF;
        bool check_integrity() {
            return true;
        }
};

class OFFReader {
    public:
        Mesh read(const string& filename) {
            ifstream infile(filename);
            string line;
            getline(infile, line);
            if (line != "OFF"){
                cerr << "Not a valid OFF file" << endl;
                throw 1;
            }
            int Nvertices, Nftriangles;
            infile >> Nvertices >> Nftriangles;
            cout << Nvertices << " vertices, " << Nftriangles << " faces" << endl;
            Mesh mesh;
            for (int i = 0; i < Nvertices; i++) {
                double x, y, z;
                infile >> x >> y >> z;
                mesh.tabV.push_back(Vertex(x, y, z, 0));
            }
            for (int i = 0; i < Nftriangles; i++) {
                int a, b, c;
                infile >> a >> b >> c;
                mesh.tabF.push_back(Triangle({a, b, c}, {0, 0, 0}));
            }
            return mesh;
        }
};

int main() {
    Mesh m;
    Vertex v1, v2, v3, v4;
    m.tabV.push_back(v1);
    m.tabV.push_back(v2);
    m.tabV.push_back(v3);
    m.tabV.push_back(v4);
    v1.set(0, 0, 0);
    v2.set(1, 0, 0);
    v3.set(0, 1, 0);
    v4.set(0, 0, 1);
    Triangle t1, t2, t3, t4;
    m.tabF.push_back(t1);
    m.tabF.push_back(t2);
    m.tabF.push_back(t3);
    m.tabF.push_back(t4);
    t1.indice_sommets = {0, 1, 2};
    t1.indice_sommets = {0, 1, 3};
    t1.indice_sommets = {0, 2, 3};
    t1.indice_sommets = {1, 2, 3};
    OFFReader reader;
    Mesh mesh = reader.read("Test1.off");
}