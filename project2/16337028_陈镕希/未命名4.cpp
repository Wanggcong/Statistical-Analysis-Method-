#include<iostream>
#include<iomanip>
using namespace std;
int main(){
	double a=16989.31278129,b=8059.72578743,c=9705.11321773,d=6730.40809095,e=17331.53343805;
	double bzc=1.96*11366.681011506962;
	cout<<"��׼���1.96�Ľ��Ϊ��"<<fixed<<setprecision(8)<<bzc<<endl;
	cout<<"��һ��Ԥ���˵���������Ϊ��["<<a-bzc<<","<<a+bzc<<"]"<<endl;
	cout<<"�ڶ���Ԥ���˵���������Ϊ��["<<b-bzc<<","<<b+bzc<<"]"<<endl;
	cout<<"������Ԥ���˵���������Ϊ��["<<c-bzc<<","<<c+bzc<<"]"<<endl;
	cout<<"���ĸ�Ԥ���˵���������Ϊ��["<<d-bzc<<","<<d+bzc<<"]"<<endl;
	cout<<"�����Ԥ���˵���������Ϊ��["<<e-bzc<<","<<e+bzc<<"]"<<endl;
} 
