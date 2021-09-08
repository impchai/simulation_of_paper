function [y1, y2]=cal_weight(V_k,N,lambda)
rng(0)
V_l=[20,30,40,50,60,70,80];
% N=500;%N为车的数量，即vt的个数
vt=normrnd(40,6,1,N);
% vt=20+40*rand(1,N);
% V_k=40;
% lambda=1;
beta=0.005;
w1=[];
for i=1:N
    if i==1
        w1(i)=Newcal_weight_incre(lambda, beta, V_l, V_k, vt(i));
    else
        w1(i)=w1(i-1)+Newcal_weight_incre(lambda, beta, V_l, V_k, vt(i));
    end
end
y1=w1;

w2=[];
for i=1:N
    if i==1
        w2(i)=Traditional_weight_incre(lambda,  V_l);
    else
        w2(i)=w2(i-1)+Traditional_weight_incre(lambda, V_l);
    end
end
y2=w2;

end


