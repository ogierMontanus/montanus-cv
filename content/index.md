---
layout: page.njk
title: Home
permalink: /
---

## Holger Berg, historian

I am a historian specialising in early modern German history, religious and cultural history, and the history of the Thirty Years War. I am currently researcher at the [Hans Christian Andersen Centre](http://andersen.sdu.dk), University of Southern Denmark, and edition philologist at the [Grundtvig Study Center](http://www.grundtvigcenteret.dk/), Aarhus University.

My research focuses on Erfurt during the Thirty Years War, the religious and cultural experience of military occupation, and the history of chronological representation. I also work on critical editions of early modern and nineteenth-century texts.

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

### Contact

University of Southern Denmark · [nh@sdu.dk](mailto:nh@sdu.dk) · [ORCID 0000-0002-8496-7221](https://orcid.org/0000-0002-8496-7221)
