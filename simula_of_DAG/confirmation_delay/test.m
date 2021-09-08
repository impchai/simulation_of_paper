clc;clear;
lambda=1;
V_l=[30,40,50];
beta=0.005;
vt=[30,40,50];
V_k=40;
t1=[];
t2=[];
for i=1:3
   [t1(i),t2(i)]=Newcal_weight_incre(lambda, beta, V_l, V_k, vt(i)); 
end
plot(t1)
