#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> a(n);
        for(int i=0;i<n;i++) cin>>a[i];
        sort(a.begin(),a.end());
        int ans=0;
        int c=0;
        int flag=0;
       for(int i=0;i<n;i++){
        for(int j=n-1;j>i;j--){
           
            if((a[i]+a[j])%2==0){
                flag=1;
                break;
            }
             c++;
        }
        if(flag==1)break;
        
       }
       flag=0;
       for(int i=n-1;i>0;i--){
        for(int j=0;j<i;j++){
            
            if((a[i]+a[j])%2==0){
                flag=1;
                break;
            }
            ans++;
        }
        if(flag==1)break;
       }
       ans=min(c,ans);
       cout<<ans<<endl;


    }
    return 0;
}