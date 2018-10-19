from oslo_utils import specs_matcher

matcher = specs_matcher

rlt = []
for n in [
    ('4', '>= 4.0'),
    ('23', '< 1.0'),
    ('123', 's< 23'),
    ('123', 's< 23'),
    (str(['foxfox']), '<all-in> o x f'),
    ('foxfox', '<in> ox <in> fo'),
    ('foxfox', '<or> foxfox'),
    ('foxfox', '<or> fox')
]:
    rlt.append(matcher.match(n[0], n[1]))

print(rlt)