---
layout: page
title: Histogram
permalink: /histogram/
parent: Plot data types
---
# Histogram
The `histogram` data type able to plot a set of value frequency diagram.

The `histogram` type is not well implemented and is not convincing in its
current form. To plot the frequency diagram of a set of values I suggest to
compute it and to plot it using the [`bar`]({{site.baseurl}}/bar/) type.
{: .danger}

## Conversion function
```python
def get_hist(data):
    freq = [0]*(max(data)+1)
    for v in data:
        freq[v] += 1
    return freq
    
data = [4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5]
freq = get_hist(data)
```

<span class="fs-4">
[Bar plot type >>]({{site.baseurl}}/bar/){: .btn}
</span>
