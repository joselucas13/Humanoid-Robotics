% ECE 590 - Humanoid Robotics
% Jose Lucas Gomes Olavo

% Inverse Kinematics in 2D

clear all
close all
clc

%%

theta = [0 0 0];
g = [0.00 0.15];
err = 0.003;
dd_theta = 0.01;
stp = 0.003;

e = get_FK(theta);

count = 0;
while(get_dist(e,g) > err)
    
    J = get_J(dd_theta, theta);
    Jp = pinv(J)
    de = get_next_point_delta(e,g,stp)
    d_theta = Jp*de'
    theta = theta + d_theta'
    theta = wrapTo2Pi(theta);
    e = get_FK(theta)
    
    
    count = count + 1 
    if (count > 500)
        break;
    end
end

d = get_dist(e,g);
disp(e);
disp(g);
disp(d);
disp(theta);
disp(theta*180/pi)
