return [{"org":"organization","com":"commercial","net":"network","info":"information"}[d.split('.')[-1]] for d in eval(dir()[0])[0]]
