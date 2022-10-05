
/*

struct Node
{
    int data;
    struct Node *next;
    Node(int x) {
        data = x;
        next = NULL;
    }

*/
class Solution
{
    public:
    //Function to check if the linked list has a loop.
    bool detectLoop(Node* head)
    {
      if(!head) return false;
      unordered_map<Node *, int>m;
      while(head)
      {
          if(!m[head])
          {
              m[head] = 1;
              head = head->next;
          }
          else return true;
      }
      return false;
    }
};
