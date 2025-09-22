" swallow copy (copies top level object , share reference of nested object)"
"deep copy (copies both top level object and nested object)"




from copy import copy as c,deepcopy

fav=[
     ["meal","sambar"],
     ["biriyani","lime"],
     ["burger","cold-coffe"]]


nan_fav=deepcopy(fav)
# nan_fav=c(fav)


nan_fav[0][0]="dosa"

print(fav)

print(nan_fav)

