% Get Forward Kinematics

function p = get_next_point_delta(e,g,stp)

m = g - e;
m = m./norm(m);

p = m*stp;
end
