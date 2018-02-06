/*Done*/
#include<bits/stdc++.h>


using namespace std;

char s[1000005];
int main(){

    int t, n, m, x, k, we_have_e, we_have_o;
    cin>>t;
    while(t--){
        we_have_e = 0, we_have_o = 0;
        cin>>n>>m>>x>>k;
        for(int i=0; i<k; ++i){
            cin>>s[i];
            if(s[i]=='E') we_have_e++;
            else we_have_o++;
        }
        int odd_months;
        if(m%2) odd_months = m/2+1;
        else odd_months = m/2;
        int even_months = m/2;
        if(we_have_e<x){
            n = n - we_have_e;
            even_months --;
        }
        else
            while(we_have_e>x && even_months>0){
                n = n-x;
                we_have_e = we_have_e-x;
                even_months--;
            }
        if(we_have_e>0 && even_months>0)
            n = n - we_have_e;

        //here
        if(we_have_o<x){
            n = n - we_have_o;
            odd_months --;
        }
        else
            while(we_have_o>x && odd_months>0){
                n = n-x;
                we_have_o = we_have_o-x;
                odd_months--;
            }
        if(we_have_o>0 && odd_months>0)
            n = n - we_have_o;
        //cout<<"odd_m = "<<odd_months<<" even_m = "<<even_months<<endl;
        if(n<=0)
            cout<<"yes\n";
        else
            cout<<"no\n";
    }
}
