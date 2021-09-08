function [t_final_pow,t_final_pod,t_final_dpos]=tradition_delay()
lambda=1:10;
blocksize=9;
blockhead=30;
%------------Generation Delay
t_gen=(blocksize./lambda+blockhead)*6 %confirmation by subsequent 6 blocks
%------------Miner Selection Delay
algs='SHA-256';
origin='testpow';
h=hash(origin,algs)
%1. standard PoW
tic
not_found = true;
iter = 1;
while( not_found)
    newHash = hash(  strcat( origin, num2str(iter) ),algs);                
    if( strcmp(newHash(1:2),'00') )
        iter              
        newHash        
        break 
    end
    iter = iter + 1;
end
t_pow=toc;
%2. Proof-of-driving(PoW with less difficulty)
tic
not_found = true;
iter = 1;
target=hash(origin,algs);
target_one=target(1);
target_two=target(2);
target_three=target(3);
target_four=target(4);
while( not_found)
    newHash = hash(  strcat( origin, num2str(iter) ),algs);
    temp1=newHash(1);
    temp2=newHash(2);
    temp3=newHash(3);
    temp4=newHash(4);
    if( hex2dec(temp1)<hex2dec(target_one) && hex2dec(temp2)<hex2dec(target_two) && hex2dec(temp3)<hex2dec(target_three))
        iter              
        newHash        
        break 
    end
    iter = iter + 1;
end
t_pod=toc;
%3. Proof-of-Storage/ DPoS (Selecting Miner by taking turn or selecting miner with the highest Storage)
t_dpos=0;

%------------Total Delay
t_final_pow=t_gen+t_pow*1000;
t_final_pod=t_gen+t_pod*1000;
t_final_dpos=t_gen+t_dpos*1000;
end
