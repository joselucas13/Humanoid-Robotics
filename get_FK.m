% Get Forward Kinematics

function e = get_FK(theta)

l1 = 0.3;
l2 = 0.2;
l3 = 0.1;

x = l1*cos(theta(1)) + l2*cos(theta(1)+theta(2)) + l3*cos(theta(1)+theta(2)+theta(3));
y = l1*sin(theta(1)) + l2*sin(theta(1)+theta(2)) + l3*sin(theta(1)+theta(2)+theta(3));

e = [x y];

end
