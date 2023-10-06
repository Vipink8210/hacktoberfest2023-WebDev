

class Solution{
  public:
    int missingNumber(vector<int>& a, int n) {
    
    int totalNm = (n*(n+1))/2;
    
    int sum =0;
    
    for(int i=0;i<n-1;i++){
        sum +=a[i];
    }
    
    return totalNm-sum;
}



};
