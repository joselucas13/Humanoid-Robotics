% Get Jacobian

function J = get_J(d_theta, theta)

e = get_FK(theta);

for i = 1 : length(e)
    for j = 1 : length(theta)
        theta_new = theta;
        theta_new(j) = theta_new(j) + d_theta;
        de = get_FK(theta_new) - e;
        
        J(i,j) = de(i)/d_theta;
    end
end
