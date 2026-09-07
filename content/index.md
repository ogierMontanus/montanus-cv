---
layout: page.njk
title: Home
permalink: /
---

## Holger Berg, historian

I am a historian with a particular focus on in early modern German and the Golden Age of Danish literature during the nineteenth century. I am employed at the [Hans Christian Andersen Centre](http://www.sdu.dk/hca), University of Southern Denmark.

### Selected publication

My monograph [*Military Occupation under the Eyes of the Lord. Studies in Erfurt during the Thirty Years War*]({{ '/books/' | url }}) (Göttingen: Vandenhoeck & Ruprecht, 2010) was defended as a Ph.D. thesis at the European University Institute in Florence in November 2008.

### Affiliations and memberships

#### Affiliations

<dl class="cv-list">
{% for item in affiliations %}
<div class="cv-entry">
  <dt class="cv-year">{{ item.years }}</dt>
  <dd class="cv-detail">{{ item.description | safe }}</dd>
</div>
{% endfor %}
</dl>

#### Memberships (selection)

<dl class="cv-list">
{% for item in memberships %}
<div class="cv-entry">
  <dt class="cv-year">{{ item.years }}</dt>
  <dd class="cv-detail">{{ item.description | safe }}</dd>
</div>
{% endfor %}
</dl>

#### Organization

<dl class="cv-list">
{% for item in organization %}
<div class="cv-entry">
  <dt class="cv-year">{{ item.years }}</dt>
  <dd class="cv-detail">{{ item.description | safe }}</dd>
</div>
{% endfor %}
</dl>

### Contact

University of Southern Denmark · [nh@sdu.dk](mailto:nh@sdu.dk) · [ORCID 0000-0002-8496-7221](https://orcid.org/0000-0002-8496-7221)
