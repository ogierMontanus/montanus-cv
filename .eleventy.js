const yaml = require("js-yaml");

module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addDataExtension("yaml", contents => yaml.load(contents));

  eleventyConfig.addFilter("filterByType", (items, ...types) =>
    (items || []).filter(p => types.includes(p.type))
  );
  eleventyConfig.addFilter("filterByFlag", (items, flag) =>
    (items || []).filter(p => p[flag] !== false)
  );
  eleventyConfig.addFilter("sortByYear", items =>
    [...(items || [])].sort((a, b) => (b.year || 0) - (a.year || 0))
  );
  eleventyConfig.addFilter("groupByDecade", items => {
    const groups = {};
    for (const item of (items || [])) {
      const decade = item.year ? Math.floor(item.year / 10) * 10 + "s" : "Undated";
      if (!groups[decade]) groups[decade] = [];
      groups[decade].push(item);
    }
    return Object.entries(groups).sort((a, b) => b[0].localeCompare(a[0]));
  });

  return {
    dir: {
      input: "content",
      includes: "../templates/_includes",
      layouts: "../templates",
      data: "../data",
      output: "_site"
    },
    templateFormats: ["njk", "md"],
    markdownTemplateEngine: "njk"
  };
};
