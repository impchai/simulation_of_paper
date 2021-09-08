function[h_incre]=Traditional_weight_incre(lambda, V_l)
len=length(V_l);
h_incre=2*lambda/len-lambda/(len*len);

end


