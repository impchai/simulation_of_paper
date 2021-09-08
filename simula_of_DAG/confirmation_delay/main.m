
t1=[];%m2-type
t2=[];%m1-type
t3=[];%standard DAG
t4=[];%standard PoW
t5=[];%Proof-of-driving
t6=[];%DPoS & Proof-of-Storage
for i=1:10
    [t1(i),t2(i),t3(i)]=time_final(i)
end
[t4,t5,t6]=tradition_delay()

x=1:10
plot(x,t1,x,t2,'-o',x,t3,'-x',x,t4,'--',x,t5,'-v',x,t6,':s', 'linewidth',2)
legend('m2-type','m1-type','Standard DAG','Standard PoW','PoD','PoS','FontSize',20)
grid on
ylabel('Confirmation Delay (ms)')
xlabel('Transaction Rate (\lambda)')
xlim([1 10])
set(gca,'FontSize',20)