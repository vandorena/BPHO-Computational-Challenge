numberstep = 1e6;
stepsize = 1;
x= zeros(1,numberstep); y = zeros(1,numberstep);

for n = 2:numberstep
    theta = 2*pi*rand;
    x(n) = x(n-1) + stepsize*cos(theta); y(n) = y(n-1) + stepsize*sin(theta);
end

plot(x,y,"b-"); hold on;
plot(x(1),y(1),"g*"); plot(x(end),y(end),"r*");


