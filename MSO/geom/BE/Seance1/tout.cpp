#include <vector>
#include <iostream>
using namespace std;

class Vertex {
    public:
        double x;
        double y;
        double z;
        int indice_tri;
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
}