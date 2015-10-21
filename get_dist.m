% Get Eucledian Distance

function d = get_dist(e,g)

tam_e = length(e);
tam_g = length(g);

sum = 0;
if tam_e == tam_g
    for i = 1 : tam_e
        sum = (e(i) - g(i))^2 + sum;
    end
    d = sqrt(sum);
end
end
