function y = objMP(data)
   a = [data{:}];
   x = cell2mat(a); 
   y = double(reshape(x,5,5));
end