                           PRINTING NEATLY
DESCRIPTION
Consider the problem of neatly printing a paragraph with a moonscape font (all characters having the same width) on a printer. 
The input text is a sequence of nn words of lengths l1,l2,…,lnl1,l2,…,ln, measured in characters.
 We want to print this paragraph neatly on a number of lines that hold a maximum of MM characters each. Our criterion of "neatness" is as follows. 
If a given line contains words ii through jj, where i=ji=j , and we leave exactly one space between words, 
the number of extra space characters at the end of the line is M-j+i-?jk=ilkM-j+i-?k=ijlk, which must be nonnegative so that the words fit on the line.
 We wish to minimize the sum, over all lines except the last, of the cubes of the numbers of extra space characters at the ends of lines. 
Give a dynamic-programming algorithm to print a paragraph of nn words neatly on a printer. Analyze the running time and space requirements of your algorithm.
Note: We assume that no word is longer than will fit into a line, i.e., li=Mli=M for all ii.
First, we'll make some definitions so that we can state the problem more uniformly.
 Special cases about the last line and worries about whether a sequence of words fits in a line will be handled in these definitions, 
so that we can forget about them when framing our overall strategy.
•Define extras[i,j]=M-j+i-?jk=ilkextras[i,j]=M-j+i-?k=ijlk to be the number of extra spaces at the end of a line containing words ii through jj.
 Note that extrasextras may be negative.
•Now define the cost of including a line containing words ii through jj in the sum we want to minimize:
lc[i,j]=???8if extras[i,j]<0 (i.e., words i,…,j don't fit),0if j=n and extras[i,j]=0 (last line costs 0),(extras[i,j])3otherwise.lc[i,j]={8if extras[i,j]<0 (i.e., words i,…,j don't fit),0if j=n 
and extras[i,j]=0 (last line costs 0),(extras[i,j])3otherwise.
By making the line cost infinite when the words don't fit on it, we prevent such an arrangement from being part of a minimal sum, and by making the cost 00 for the last line (if the words fit), 
we prevent the arrangement of the last line from influencing the sum being minimized.
We want to minimize the sum of lclc over all lines of the paragraph.
Our subproblems are how to optimally arrange words 1,…,j1,…,j, where j=1,…,nj=1,…,n.
Consider an optimal arrangement of words 1,…,j1,…,j. Suppose we know that the last line, which ends in word jj, begins with word ii. The preceding lines, therefore, contain words 1,…,i-11,…,i-1. 
In fact, they must contain an optimal arrangement of words 1,…,i-11,…,i-1. (The usual type of cut-and-paste argument applies.)
Let c[j]c[j] be the cost of an optimal arrangement of words 1,…,j1,…,j.
 If we know that the last line contains words i,…,ji,…,j, then c[j]=c[i-1]+lc[i,j]c[j]=c[i-1]+lc[i,j]. As a base case, when we're computing c[1]c[1], we need c[0]c[0]. If we set c[0]=0c[0]=0, then c[1]=lc[1,1]c[1]=lc[1,1], which is what we want.
But of course we have to figure out which word begins the last line for the subproblem of words 1,…,j1,…,j. 
So we try all possibilities for word ii, and we pick the one that gives the lowest cost. Here, ii ranges from 11 to jj. Thus, we can define c[j]c[j] recursively by
c[j]={0if j=0,min1=i=j(c[i-1]+lc[i,j])if j>0.c[j]={0if j=0,min1=i=j(c[i-1]+lc[i,j])if j>0.
Note that the way we defined lclc ensures that
•	all choices made will fit on the line (since an arrangement with lc=8lc=8 cannot be chosen as the minimum), and
•	the cost of putting words i,…,ji,…,j on the last line will not be 00 unless this really is the last line of the paragraph (j=nj=n) or words i,…,ji,…,j fill the entire line.
We can compute a table of cc values from left to right, since each value depends only on earlier values.
To keep track of what words go on what lines, we can keep a parallel pp table that points to where each cc value came from. When c[j]c[j] is computed, if c[j]c[j] is based on the value of c[k-1]c[k-1], set p[j]=kp[j]=k. Then after c[n]c[n] is computed, we can trace the pointers to see where to break the lines. The last line starts at word p[n]p[n] and goes through word nn. The previous line starts at word p[p[n]]p[p[n]]and goes through word p[n]-1p[n]-1, et.


Quite clearly, both the time and space are T(n2)T(n2).
In fact, we can do a bit better: we can get both the time and space down to T(nM)T(nM). The key observation is that at most ?M/2??M/2? words can fit on a line. (Each word is at least one character long, and there's a space between words.) Since a line with words i,…,ji,…,j contains j-i+1j-i+1words, if j-i+1>?M/2?j-i+1>?M/2? then we know that lc[i,j]=8lc[i,j]=8. We need only compute and store extras[i,j]extras[i,j] and lc[i,j]lc[i,j] for j-i+1=?M/2?j-i+1=?M/2?. And the inner for loop header in the computation of c[j]c[j] and p[j]p[j] can run from max(1,j-?M/2?+1)max(1,j-?M/2?+1) to jj.
We can reduce the space even further to T(n)T(n). We do so by not storing the lclc and extrasextras tables, and instead computing the value of lc[i,j]lc[i,j] as needed in the last loop. The idea is that we could compute lc[i,j]lc[i,j] in O(1)O(1) time if we knew the value of extras[i,j]extras[i,j]. And if we scan for the minimum value in descending order of ii, we can compute that as extras[i,j]=extras[i+1,j]-li-1extras[i,j]=extras[i+1,j]-li-1. (Initially, extras[j,j]=M-ljextras[j,j]=M-lj.) This improvement reduces the space to T(n)T(n), since now the only tables we store are cc and pp.
Here's how we print which words are on which line. The printed output of GIVE-LINES(p,j)GIVE-LINES(p,j) is a sequence of triples (k,i,j)(k,i,j), indicating that words i,…,ji,…,j are printed on line kk. The return value is the line number kk.
