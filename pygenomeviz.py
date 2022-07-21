from pygenomeviz import GenomeViz

genome_list = (
    {"name": "A4hap1", "size": 72890, "cds_list": [[1,477, 1], [18969,19348, -1], [24164,25191, -1], [27044,27364, -1], [29496,29961, -1], [34281,35163, -1], [35941,36595, -1], [37656,39161, -1], [39370,40218, 1], [40576,42567, 1], [43919,45426, -1], [56088,56752, 1], [58331,58759, +1], [60450,62956, +1], [72164,72890, +1]]},
    #{ "name": "A4hap2", "size": 65688, "cds_list": [[1,1043, 1], [2930,3256,-1], [5642,6297, 1],[8227,8877, -1],[13080,13391, -1], [19788, 21068,-1], [21205,21979, -1], [22262,23596, -1], [23979,24905, 1], [25268,27256, 1], [37377,40358, -1], [45257,47166, 1], [64962,65688, 1] ]}
        { "name": "A4hap2", "size": 65688, "cds_list": [[5642,6297, 1],[13080,13391, -1], [19788, 21068,-1], [21205,21979, -1], [22262,23596, -1], [23979,24905, 1], [25268,27256, 1], [37377,40358, -1], [45257,47166, 1], [64962,65688, 1] ]}
)

ortholog_genes = [[34281, 35163, -1], [19788, 21068, -1], [35941, 36595, -1], [21205, 21979, -1], [37656, 39161, -1], [22262, 23596, -1], [39370, 40218, 1], [ 23979, 24905, 1],
 [40576, 42567, 1], [25268, 27256, 1], [72164, 72890, 1], [64962, 65688, 1], [29496,29961, -1],[24164,25191, -1]]

pseudogenes = [[5642,6297, 1], [13080,13391, -1]]

gv = GenomeViz(tick_style="axis", fig_track_height=1.5, feature_track_ratio=0.5)

plotstyles = ("bigarrow", "arrow", "bigbox", "box", "bigrbox", "rbox")
colors = ("orange", "blue", "lime", "red")
for genome in genome_list:
    name, size, cds_list = genome["name"], genome["size"], genome["cds_list"]
    track = gv.add_feature_track(name, size, labelmargin=0.03, linecolor="black", linewidth=3)
    for idx, cds in enumerate(cds_list, 1):
        if cds in ortholog_genes:
            start, end, strand = cds
            track.add_feature(
                    start,
                    end,
                    strand,
                    #label=f"gene{idx:02d}",
                    #labelsize=12,
                    #labelcolor="white",
                    facecolor="green",
                    plotstyle= "bigarrow",
                    linewidth=1,
                    labelrotation=0,
                    labelvpos="center",
                    labelhpos="center",
                    labelha="center",
                    #arrow_shaft_ratio=1.0,
                )
        elif cds in pseudogenes:
            start, end, strand = cds
            track.add_feature(
                    start,
                    end,
                    strand,
                    #label=f"gene{idx:02d}",
                    #labelsize=12,
                    #labelcolor="white",
                    facecolor="black",
                    plotstyle= "bigarrow",
                    linewidth=1,
                    labelrotation=0,
                    labelvpos="center",
                    labelhpos="center",
                    labelha="center",
                    #arrow_shaft_ratio=1.0,
                )
        else:
            start, end, strand = cds
            track.add_feature(
                    start,
                    end,
                    strand,
                    #label=f"gene{idx:02d}",
                    #labelsize=12,
                    #labelcolor="white",
                    facecolor="red",
                    linewidth=1,
                    labelrotation=0,
                    labelvpos="center",
                    labelhpos="center",
                    labelha="center",
                   # arrow_shaft_ratio=1.0,
                )
# Add links between "genome 01" and "genome 02"
gv.add_link(("A4hap1", 34281, 35163), ("A4hap2", 19788, 21068),normal_color="grey", curve=True)
gv.add_link(("A4hap1", 35941, 36595), ("A4hap2", 21205, 21979),normal_color="grey", curve=True)
gv.add_link(("A4hap1", 37656, 39161), ("A4hap2", 22262, 23596),normal_color="grey", curve=True)
gv.add_link(("A4hap1", 39370, 40218), ("A4hap2", 23979, 24905),normal_color="grey", curve=True)
gv.add_link(("A4hap1", 40576, 42567), ("A4hap2", 25268, 27256),normal_color="grey", curve=True)
gv.add_link(("A4hap1", 72164, 72890), ("A4hap2",64962, 65688), normal_color="grey", curve=True)
gv.add_link(("A4hap1", 29496,29961), ("A4hap2",13080,13391 ), normal_color="skyblue")
gv.add_link(("A4hap1", 24164,25191), ("A4hap2", 5642,6297), normal_color="skyblue")

fig = gv.plotfig(dpi=300)
