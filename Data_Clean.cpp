#include<bits/stdc++.h>
#define pf printf
#define sf scanf
#define ll long long
#define llu unsigned long long
#define M 100000
#define pb push_back
#define ppb pop_back
#define F first
#define S second
#define Check(x,w) (x&(1<<w))==(1<<w)?true:false
#define pii pair<ll,ll>
#define pvi pair<vector<int>,int>
#define EPS 1e-5
#define PI acos(-1)
#define Mems(p,n) memset(p,n,sizeof(p))
#define MOD 1000000007
#define inf -2000000000;
#define INT(c)  ((int)((c) - '0'))
#define CHAR(i) ((char)(i + int('0')))
using namespace std;

template<class T>
inline bool fs(T &x)
{
    int c=getchar();
    int sgn=1;
    while(~c&&c<'0'||c>'9')
    {
        if(c=='-')sgn=-1;
        c=getchar();
    }
    for(x=0; ~c&&'0'<=c&&c<='9'; c=getchar())
        x=x*10+c-'0';
    x*=sgn;
    return ~c;
}

struct data
{
    double point1,point2,point3;
    int pre,on,post;
    double time;
    string lan, lot;
    vector<string>status;
};

vector<data>ans;
double best_ratio=0.75;

string pre[]={"ready", "warning", "alerts", "preparedness", "safety", "tornadosafety",
                "staysafe", "declaration", "plan", "prepared", "tornadowarning",
                "takecover", "ready", "awareness", "Alert", "Beware", "prepared", "EmergencyPreparedness",
                 "FloodReady", "HaveAPlan",  "team", "emergency"};
int pre_len=21;

string on[]={"thunderstorm", "outbreaks", "snowstorm", "lightning", "blizzard", "clouds", "rain",
              "badweather", "stormchasers", "pray", "Drowning", "overflow", "damaging", "wind",
              "sky", "flooding", "flood", "after", "stay"};
int on_len=19;

string post[]={"disasterrecovery", "shelter","donations", "recovery", "victims", "rebuilding",
                "damaged", "relief", "house", "response", "responder", "help", "helping",
                "Disaster Solutions", "FLOOD DAMAGE", "dead", "effects", "volunteers", "restoration",
                "impacts", "survivors", "EmergencyRelief", "startup", "experienced", "team", "storng"};
int post_len=26;

#define psi pair<string,string>
map<psi,int>mp;

string s,t,u,v;

bool comp(data a,data b)
{
    if(a.time==b.time)
    {
        if(a.point1==b.point1)
        {
            if(a.point2==b.point2)
            {
                if(a.point3==b.point3)
                    return a.time<b.time;
                return a.point3<b.point3;
            }
            return a.point2<b.point2;
        }
        return a.point1<b.point1;
    }
    return a.time<b.time;
}

int month_conversion(string a)
{
    if(a=="Jan")
        return 0;
    if(a=="Feb")
        return 31;
    if(a=="Mar")
        return 31+28;
    if(a=="Apr")
        return 31+28+31;
    if(a=="May")
        return 31+28+31+30;
    if(a=="Jun")
        return 31+28+31+30+31;
    if(a=="Jul")
        return 31+28+31+30+31+30;
    if(a=="Aug")
        return 31+28+31+30+31+30+31;
    if(a=="Sep")
        return 31+28+31+30+31+30+31+31;
    if(a=="Oct")
        return 31+28+31+30+31+30+31+31+30;
    if(a=="Nov")
        return 31+28+31+30+31+30+31+31+30+31;
    if(a=="Dec")
        return 31+28+31+30+31+30+31+31+30+31+30;
    return 365;
}

vector<string>tweet;
vector<string>buffer;

int main()
{
    //freopen("Debbie2-Phase3.txt","r",stdin);
    //freopen("Debbie2-Phase3-clean.txt","w",stdout);
    psi xx;
    xx.F="response";
    xx.S="way";
    mp[xx]=1;
    xx.F="safety";
    xx.S="damaged";
    mp[xx]=3;
    xx.F="house";
    xx.S="will";
    mp[xx]=1;
    xx.F="damaged";
    xx.S="will";
    mp[xx]=1;
    xx.F="help";
    xx.S="can";
    mp[xx]=1;
    xx.F="shelter";
    xx.S="will";
    mp[xx]=1;
    xx.F="prepared";
    xx.S="was";
    mp[xx]=3;
    xx.F="rain";
    xx.S="coming";
    mp[xx]=1;
    xx.F="sky";
    xx.S="was";
    mp[xx]=1;
    xx.F="wind";
    xx.S="coming";
    mp[xx]=1;
    xx.F="wind";
    xx.S="start";
    mp[xx]=1;
    xx.F="cloud";
    xx.S="coming";
    mp[xx]=1;
    xx.F="volunteer";
    xx.S="join";
    mp[xx]=1;
    xx.F="rain";
    xx.S="stop";
    mp[xx]=3;
    xx.F="rain";
    xx.S="calm";
    mp[xx]=3;
    xx.F="safety";
    xx.S="working";
    mp[xx]=3;
    xx.F="help";
    xx.S="times";
    mp[xx]=2;
    int a,b,c,d,e,f,g,h,i,j;
    double x,y;
    int p1=0,p2=0,p3=0;
    double r=1000000000000.0,q=0.0;
    string lan1,lot1;
    int cnts=0;
    while(cin>>s)
    {
        if(s=="#$%%$#")
        {
            if(p1==0 && p2==0 && p3==0)
            {
                x=0.0;
                tweet.clear();
                continue;
            }
            for(i=0; i<tweet.size(); i++)
            {
                transform(tweet[i].begin(), tweet[i].end(), tweet[i].begin(), ::tolower);
            }
            for(i=0; i<buffer.size(); i++)
            {
                for(j=0; j<tweet.size(); j++)
                {
                    xx.F=buffer[i];
                    xx.S=tweet[j];
                    int aa=mp[xx];
                    if(aa==1)
                        p1+=1;
                    if(aa==2)
                        p2+=1;
                    if(aa==3)
                        p3+=1;
                }
            }
            data w;
            w.point1=(double)p1;
            w.point2=(double)p2;
            w.point3=(double)p3;
            w.time=x;
            w.status=tweet;
            w.lan=lan1;
            w.lot=lot1;
            if(w.lot!="-1" && w.lan!="-1")
                cnts++;
            ans.pb(w);
            r=min(r,x);
            q=max(q,x);
            p1=0;
            p2=0;
            p3=0;
            x=0.0;
            tweet.clear();
            buffer.clear();
            continue;
        }

        if(s=="@Oshy@")
        {
            cin>>u;
            cin>>u;
            cin>>u;
            a=month_conversion(u);
            cin>>u;
            b=((u[0]-'0')*10)+(u[1]-'0');
            a+=b;
            cin>>u;
            c=((u[0]-'0')*10)+(u[1]-'0');
            c*=3600;
            d=((u[3]-'0')*10)+(u[4]-'0');
            d*=60;
            e=((u[6]-'0')*10)+(u[7]-'0');
            c+=d+e;
            y=((double)c*1.0);
            x=(double)y/double(60.0);
            cin>>u;
            cin>>u;
            c=((u[0]-'0')*1000)+((u[1]-'0')*100)+((u[2]-'0')*10)+(u[3]-'0');
            c-=2000;
            c*=365;
            c+=a;
            y=((double)c*1.0*24*60);
            x+=(double)y;
            cin>>lan1>>lot1;
            continue;
        }
        tweet.pb(s);
        for(i=0; i<pre_len; i++)
        {
            a=pre[i].size();
            b=s.size();
            if(s=="")
                break;
            c=0;
            d=0;
            if(s[0]=='#')
                c=1;
            while(d<a && c<b)
            {
                if(tolower(s[c])!=tolower(pre[i][d]))
                    break;
                c++;
                d++;
            }
            if(d==a && c==b)
                p1+=1,buffer.pb(pre[i]);
            else if(c+1<b && (s[c+1]=='.' || s[c+1]==',' || s[c+1]=='?' || s[c+1]=='!') && a==d)
                p1+=1,buffer.pb(pre[i]);
            else if(c+1==b && d==a)
                p1+=1,buffer.pb(pre[i]);

        }

        for(i=0; i<on_len; i++)
        {
            a=on[i].size();
            b=s.size();
            if(s=="")
                break;
            c=0;
            d=0;
            if(s[0]=='#')
                c=1;
            while(d<a && c<b)
            {
                if(tolower(s[c])!=tolower(on[i][d]))
                    break;
                c++;
                d++;
            }
            if(d==a && c==b)
                p2+=1,buffer.pb(on[i]);
            else if(c+1<b && (s[c+1]=='.' || s[c+1]==',' || s[c+1]=='?' || s[c+1]=='!') && d==a)
                p2+=1,buffer.pb(on[i]);
            else if(c+1==b && d==a)
                p2+=1,buffer.pb(on[i]);

        }

        for(i=0; i<post_len; i++)
        {
            a=post[i].size();
            b=s.size();
            if(s=="")
                break;
            c=0;
            d=0;
            if(s[0]=='#')
                c=1;
            while(d<a && c<b)
            {
                if(tolower(s[c])!=tolower(post[i][d]))
                    break;
                c++;
                d++;
            }
            if(d==a && c==b)
                p3+=1,buffer.pb(post[i]);
            else if(c+1<b && (s[c+1]=='.' || s[c+1]==',' || s[c+1]=='?' || s[c+1]=='!') && a==d)
                p3+=1,buffer.pb(post[i]);
            else if(c+1==b && d==a)
                p3+=1,buffer.pb(post[i]);
        }
    }
    q=q-r;
    sort(ans.begin(),ans.end(),comp);
    for(i=0; i<ans.size(); i++)
    {
        ans[i].point1=ans[i].point1*best_ratio*q;
        ans[i].point2=ans[i].point2*best_ratio*q;
        ans[i].point3=ans[i].point3*best_ratio*q;
        ans[i].time-=((double)r);
        ans[i].pre=ans[i].on=ans[i].post=0;
        if(ans[i].point1==ans[i].point2 && ans[i].point2==ans[i].point3)
        {
            ans[i].pre=ans[i].on=ans[i].post=1;
            pf("%.3lf,%.3lf,%.3lf,%.3lf,%d,%d,%d",ans[i].point1,ans[i].point2,ans[i].point3,ans[i].time,ans[i].pre,ans[i].on,ans[i].post);
        }
        else if(ans[i].point1==ans[i].point2 && ans[i].point1>ans[i].point3)
        {
            ans[i].pre=ans[i].on=1;
            pf("%.3lf,%.3lf,%.3lf,%.3lf,%d,%d,%d",ans[i].point1,ans[i].point2,ans[i].point3,ans[i].time,ans[i].pre,ans[i].on,ans[i].post);
        }
        else if(ans[i].point1==ans[i].point3 && ans[i].point1>ans[i].point2)
        {
            ans[i].pre=ans[i].post=1;
            pf("%.3lf,%.3lf,%.3lf,%.3lf,%d,%d,%d",ans[i].point1,ans[i].point2,ans[i].point3,ans[i].time,ans[i].pre,ans[i].on,ans[i].post);
        }
        else if(ans[i].point2==ans[i].point3 && ans[i].point2>ans[i].point1)
        {
            ans[i].on=ans[i].post=1;
            pf("%.3lf,%.3lf,%.3lf,%.3lf,%d,%d,%d",ans[i].point1,ans[i].point2,ans[i].point3,ans[i].time,ans[i].pre,ans[i].on,ans[i].post);
        }
        else if(ans[i].point1>ans[i].point2 && ans[i].point1>ans[i].point3)
            ans[i].pre=1,pf("%.3lf,%.3lf,%.3lf,%.3lf,%d,%d,%d",ans[i].point1,ans[i].point2,ans[i].point3,ans[i].time,ans[i].pre,ans[i].on,ans[i].post);
        else if(ans[i].point2>ans[i].point3)
            ans[i].on=1,pf("%.3lf,%.3lf,%.3lf,%.3lf,%d,%d,%d",ans[i].point1,ans[i].point2,ans[i].point3,ans[i].time,ans[i].pre,ans[i].on,ans[i].post);
        else
            ans[i].post=1,pf("%.3lf,%.3lf,%.3lf,%.3lf,%d,%d,%d",ans[i].point1,ans[i].point2,ans[i].point3,ans[i].time,ans[i].pre,ans[i].on,ans[i].post);
        cout<<","<<ans[i].lan<<","<<ans[i].lot<<endl;
        /*for(j=0; j<ans[i].status.size(); j++)
            cout<<ans[i].status[j]<<" ";
        cout<<endl;*/
    }
    pf("\n\n%d\n",cnts);
    return 0;
}
