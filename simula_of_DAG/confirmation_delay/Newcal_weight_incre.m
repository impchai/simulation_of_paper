function[h_incre]=Newcal_weight_incre(lambda, beta, V_l, V_k, vt)
% V_l=[20,30,40,50,60,70,80];



len=length(V_l);
fl=-beta*(V_l-V_k).*(V_l+V_k-2*vt);
temp=0;
for i=1:len
    for j=1:len
        temp=temp+exp(fl(i))*exp(fl(j));
    end
end
h_incre=2*lambda/sum(exp(fl))-lambda/temp;


% temp3=exp(-beta*(V_k-vt)*((V_k-vt)));
% temp4=0;
% for i=1:len
%     temp4=temp4+exp(-beta*(V_l(i)-vt)*((V_l(i)-vt)));
% end
% h_temp=temp3/temp4;
% h_compare=2*lambda*h_temp-lambda*h_temp*h_temp;

end


