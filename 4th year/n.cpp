#include<iostream>
#include<cmath>
#include<ctime>
#include<cstdlib>
#include<fstream>
#include<algorithm>
using namespace std;

void r1(int N, int n)
{
    ofstream fout("rand.dat");
    srand(time(NULL));
    int a[N], r, b[2*n+1], x;
    /*double p[2*n+1];*/
    for(int i=0; i<=N; i++)
    {   
        x=0;
        r=(rand()%n)+1;
        for(int j=0; j<=r; j++)
        {
            double s = (double)rand()/(double)RAND_MAX;
            if(s>0.5)
            {
                x+=1;
            }
            else
            {
                x-=1;
            }
        }
        a[i]=x;
        cout << a[i] << endl;
    }

    //int b[2*n+1];
    for(int i=-n; i<=n; i++)
    {
        for(int j=0; j<=N; j++)
        {
            if(i == a[j])
            {
                b[i+n]++;
            }
        }
    }

    double p[2*n+1];

    for(int i=0; i<=2*n+1; i++)
    {
        p[i] = (double)b[i]/(double)N;
        if(p[i]!=0)
        {
            fout << i-n << "  " << p[i] << endl;
        }
    }

}

int main()
{
    int N, n;
    cout << "Enter iteratoin number: " << endl;
    cin >> N;
    cout << "Enter step number(need to smaller than iteratoin number): " << endl;
    cin >> n;
    
    if(N<=n)
    {
        cout << N << "  " << n << endl;
        N = N+n;
        n = N-n;
        N = N-n;
        r1(N,n);  
    }
    return 0;
}