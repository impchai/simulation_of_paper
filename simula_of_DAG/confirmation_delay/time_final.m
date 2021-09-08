function[y1,y2,y3]=time_final(lambda)
treshold=50;
w1=cell(1,7);
w2=cell(1,7);
N=300;



for i=1:7
    V_k=10+i*10;%V_k={20,30,40,50,60,70,80}
    [w1{1,i}, w2{1,i}]=cal_weight(V_k,N,lambda);
end

t1=[];
t2=[];
for i=1:7
    t1(i)=authen_delay(w1{1,i},treshold);
    t2(i)=authen_delay(w2{1,i},treshold);
end
y1=t1(3);
y2=t1(5);
y3=t2(1);
end





% x=1:500
% plot(x,w{1,1},x,w{1,2},x,w{1,3},x,w{1,4},x,w{1,5},x,w{1,6},x,w{1,7})
% legend('1','2','3','4','5','6','7')