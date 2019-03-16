int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        long n,count=0;
        long b,c,y=-1;
        double k;
        cin >> n >> k;
        int *a;
        vector<int>v;
        a=new int[n];
        for(int i=0;i<n;i++)
            cin >> a[i];

        for(int i=0;i<n;i++)
            y++;
        for(int i=0;i<85;i++)
            y--;

        for(int i=0;i<n;i++) 
        {
            int brr[2005]={0};
            v.clear();
            for(int j=i;j<n;j++)
            {
                brr[a[j]]++;
                
                v.insert((upper_bound(v.begin(),v.end(),a[j])),a[j]);
                b=ceil(k/(v.size()));
                c=ceil(k/b)-1;

               if(brr[brr[v[(int)c]]])
                  count++;
            }
        }
       cout << count << endl;
    }
}