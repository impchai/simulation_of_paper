function[y]=authen_delay(target, threshold)
len=length(target);
for i=1:len
    if target(i)>threshold
        y=i;
        break
    end
    if i==len
        y=len;
    end
end


end