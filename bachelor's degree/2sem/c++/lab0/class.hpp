#include <iostream>
#include <cmath>
using namespace std;

class Cylinder
{
private:
    double m_R; 
    double m_H;
    const double Pi = acos(-1);
public:
    Cylinder()
    {
        m_H = 0; m_R = 0;
    };

    Cylinder(double r, double h)
    {
        m_R = r; m_H = h;
    }

    ~Cylinder() {};

    bool Set(double R, double H)
    {
        if (R <= 0 || H <= 0) 
        {
            cout << "Error side!" << endl; 
            return false;
        }
        m_R = R; m_H = H;
        return true;
    }

    double getR() {return m_R;}
    double getH() {return m_H;}

    double getBaseArea() const
    {
        double S = Pi * pow(m_R, 2);
        return S;
    }

    double getFigureVolume() const
    {
        double V = Pi * pow(m_R, 2) * (m_H);
        return V;
    }

    void r_x10(double &r)
    {
        r *= 10;
    }

    void print1(double s1, double v1)
    {
        cout << endl << "Area of first base: " << s1 << endl;
        cout << "Volume of first figure: " << v1 << endl << endl;
    }

    void print2(double s2, double v2)
    {
        cout << "Area of second base: " << s2 << endl;
        cout << "Volume of second figure: " << v2 << endl << endl;
    }
};
