numberstep = 1e6;
stepsize = 4;
x= zeros(1,numberstep); y = zeros(1,numberstep); z = zeros(1,numberstep);

for n = 2:numberstep
    theta = 2*pi*rand;
    phi = acos(2*rand()-1);
    x(n) = x(n-1) + (stepsize*cos(theta)*sin(phi));
    y(n) = y(n-1) + (stepsize*sin(theta)*sin(phi));
    z(n) = z(n-1) + (stepsize*cos(phi));
end

figure;
plot3(x,y,z,"b-"); hold on;
plot3(x(1),y(1),z(1),"g*"); plot3(x(end),y(end),z(end),"r*");
