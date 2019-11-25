void bfs(int s, vector<int> adj[], bool vis[], int N)
{
    // Your code here
    queue<int> myqueue;
    if(vis[s]==false)
    {
        cout<<s<<" ";
        vis[s]=true;
    }
    myqueue.push(s);
    while(!myqueue.empty())
    {
        int temp = myqueue.front();
        myqueue.pop();
        for(int i=0; i<adj[temp].size(); i++)
        {
            if(vis[adj[temp][i]]==false)
            {
                cout<<adj[temp][i]<<" ";
                myqueue.push(adj[temp][i]);
                vis[adj[temp][i]]=true;
            }
        }
    }
}
