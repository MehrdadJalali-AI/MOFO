import pandas as pd
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, OWL, SKOS

# Read the dataset
df = pd.read_csv('MOFData100.csv')

# Define ontology namespaces
user = Namespace("http://MOFO.org/user/")
prop = Namespace("http://MOFO.org/property/")

# Create RDF graph
g = Graph()

# Bind namespaces
g.bind("user", user)
g.bind("prop", prop)
g.bind("skos", SKOS)

# Define classes for MOF materials
g.add((user["MOFMaterial"], RDF.type, OWL.Class))
g.add((user["Dimensionality"], RDF.type, OWL.Class))
g.add((user["Topology"], RDF.type, OWL.Class))
g.add((user["Functionality"], RDF.type, OWL.Class))
g.add((user["CrystalSystem"], RDF.type, OWL.Class))

# Define subclass relationships
g.add((user["Dimensionality"], RDFS.subClassOf, user["MOFMaterial"]))
g.add((user["Topology"], RDFS.subClassOf, user["MOFMaterial"]))
g.add((user["Functionality"], RDFS.subClassOf, user["MOFMaterial"]))
g.add((user["CrystalSystem"], RDFS.subClassOf, user["MOFMaterial"]))

# Define subclass relationships for Dimensionality
g.add((user["One_D"], RDFS.subClassOf, user["Dimensionality"]))
g.add((user["Two_D"], RDFS.subClassOf, user["Dimensionality"]))
g.add((user["Three_D"], RDFS.subClassOf, user["Dimensionality"]))

# Define subclass relationships for Crystal System
g.add((user["Triclinic"], RDFS.subClassOf, user["CrystalSystem"]))
g.add((user["Monoclinic"], RDFS.subClassOf, user["CrystalSystem"]))
g.add((user["Orthorhombic"], RDFS.subClassOf, user["CrystalSystem"]))
g.add((user["Tetragonal"], RDFS.subClassOf, user["CrystalSystem"]))
g.add((user["Trigonal"], RDFS.subClassOf, user["CrystalSystem"]))
g.add((user["Hexagonal"], RDFS.subClassOf, user["CrystalSystem"]))

# Define subclass relationships for Topology
g.add((user["IsoreticularMOFs"], RDFS.subClassOf, user["Topology"]))
g.add((user["ZeoliticImidazolateFrameworks"], RDFS.subClassOf, user["Topology"]))
g.add((user["MetalCarboxylateFrameworks"], RDFS.subClassOf, user["Topology"]))

# Define subclass relationships for Functionality
g.add((user["GasStorageAndSeparation"], RDFS.subClassOf, user["Functionality"]))
g.add((user["Catalysis"], RDFS.subClassOf, user["Functionality"]))
g.add((user["Sensors"], RDFS.subClassOf, user["Functionality"]))
g.add((user["DrugDelivery"], RDFS.subClassOf, user["Functionality"]))

# Add annotations for classes
g.add((user["Dimensionality"], SKOS.definition, Literal("Classification of MOF materials based on their dimensional structure (1D, 2D, or 3D).")))
g.add((user["Topology"], SKOS.definition, Literal("Classification of MOF materials based on their structural topology (e.g., isoreticular MOFs, zeolitic imidazolate frameworks, metal-carboxylate frameworks).")))
g.add((user["Functionality"], SKOS.definition, Literal("Classification of MOF materials based on their intended functionality (e.g., gas storage and separation, catalysis, sensors, drug delivery).")))

# Add detailed explanations using SKOS for each class
g.add((user["One_D"], SKOS.definition, Literal("1D MOFs (Metal-Organic Frameworks) are a subclass of MOFs, which are porous materials constructed from metal ions or clusters linked together by organic ligands. In 1D MOFs, the framework structure extends predominantly in one dimension. This means that the metal-ligand connectivity forms long, linear chains or threads. These structures offer unique properties and potential applications due to their elongated geometry, such as in gas storage, separation, catalysis, and sensing.")))
g.add((user["Two_D"], SKOS.definition, Literal("2D MOFs (Metal-Organic Frameworks) are a subclass of MOFs, which are porous materials constructed from metal ions or clusters linked together by organic ligands. In 2D MOFs, the framework structure extends predominantly in two dimensions, resulting in sheet-like structures. These structures offer unique properties and potential applications due to their planar geometry, such as in membrane separation, catalysis, and electronic devices.")))
g.add((user["Three_D"], SKOS.definition, Literal("3D MOFs (Metal-Organic Frameworks) are a subclass of MOFs, which are porous materials constructed from metal ions or clusters linked together by organic ligands. In 3D MOFs, the framework structure extends in three dimensions, forming a network of interconnected pores. These structures offer unique properties and potential applications due to their high porosity and large surface area, such as in gas storage, separation, catalysis, drug delivery, and sensing.")))
g.add((user["IsoreticularMOFs"], SKOS.definition, Literal("Isoreticular MOFs are a subclass of MOFs characterized by their ability to maintain the same underlying topology or framework structure across different chemical compositions and guest molecules. This means that despite variations in the metal ions, organic linkers, or functional groups, isoreticular MOFs exhibit identical pore sizes, shapes, and connectivity patterns. This uniformity enables predictable properties and versatile applications in areas such as gas storage, separation, catalysis, and drug delivery.")))
g.add((user["ZeoliticImidazolateFrameworks"], SKOS.definition, Literal("Zeolitic Imidazolate Frameworks (ZIFs) are a subclass of MOFs composed of metal ions or clusters coordinated by imidazolate-based organic linkers. ZIFs are structurally similar to zeolites, with crystalline frameworks featuring microporous channels and high thermal stability. These properties make ZIFs promising materials for gas storage, separation, catalysis, and sensing applications.")))
g.add((user["MetalCarboxylateFrameworks"], SKOS.definition, Literal("Metal Carboxylate Frameworks are a subclass of MOFs formed by the coordination of metal ions or clusters with carboxylate-based organic linkers. These frameworks exhibit diverse structures and properties depending on the choice of metal ions, ligands, and synthesis conditions. Metal carboxylate frameworks have shown potential applications in gas storage, separation, catalysis, drug delivery, and luminescence.")))
g.add((user["GasStorageAndSeparation"], SKOS.definition, Literal("MOFs designed for gas storage and separation applications are characterized by their high surface area, tunable pore sizes, and selective adsorption properties. These materials offer advantages in storing, separating, and delivering gases such as hydrogen, methane, carbon dioxide, and volatile organic compounds. Applications include gas storage for alternative energy, purification of industrial gases, and removal of pollutants from air and water.")))
g.add((user["Catalysis"], SKOS.definition, Literal("MOFs designed for catalysis applications are tailored to enhance chemical reactions by providing active sites for catalytic processes. These materials offer advantages such as high surface area, tunable porosity, and adjustable chemical environments. Applications include heterogeneous catalysis for organic synthesis, environmental remediation, and energy conversion processes such as hydrogenation, oxidation, and photocatalysis.")))
g.add((user["Sensors"], SKOS.definition, Literal("MOFs designed for sensor applications are engineered to detect specific analytes or stimuli with high sensitivity, selectivity, and response speed. These materials offer advantages such as large surface area, tailored pore sizes, and functionalization with recognition elements. Applications include gas sensors for environmental monitoring, chemical sensors for industrial processes, and biosensors for medical diagnostics.")))
g.add((user["DrugDelivery"], SKOS.definition, Literal("MOFs designed for drug delivery applications are utilized to encapsulate, transport, and release therapeutic agents with controlled release kinetics. These materials offer advantages such as high loading capacity, biocompatibility, and stimuli-responsive behavior. Applications include targeted drug delivery for cancer therapy, antimicrobial agents for infection treatment, and gene delivery vectors for genetic therapy.")))
g.add((user["Triclinic"], SKOS.definition, Literal("Triclinic crystal system MOFs have three unequal crystallographic axes and angles.")))
g.add((user["Monoclinic"], SKOS.definition, Literal("Monoclinic crystal system MOFs have one axis that is perpendicular to a plane of symmetry.")))
g.add((user["Orthorhombic"], SKOS.definition, Literal("Orthorhombic crystal system MOFs have three mutually perpendicular axes of different lengths.")))
g.add((user["Tetragonal"], SKOS.definition, Literal("Tetragonal crystal system MOFs have three mutually perpendicular axes of different lengths, but two of them are equal.")))
g.add((user["Trigonal"], SKOS.definition, Literal("Trigonal crystal system MOFs have three equal axes that are not perpendicular to each other.")))
g.add((user["Hexagonal"], SKOS.definition, Literal("Hexagonal crystal system MOFs have three equal axes that are perpendicular to each other, with a fourth axis perpendicular to the plane defined by the first three axes.")))

# Add labels in other languages using SKOS
g.add((user["Dimensionality"], SKOS.prefLabel, Literal("Dimensionalität", lang="de")))
g.add((user["Topology"], SKOS.prefLabel, Literal("Topologie", lang="de")))
g.add((user["Functionality"], SKOS.prefLabel, Literal("Funktionalität", lang="de")))
g.add((user["One_D"], SKOS.prefLabel, Literal("1D-Struktur", lang="de")))
g.add((user["Two_D"], SKOS.prefLabel, Literal("2D-Struktur", lang="de")))
g.add((user["Three_D"], SKOS.prefLabel, Literal("3D-Struktur", lang="de")))
g.add((user["IsoreticularMOFs"], SKOS.prefLabel, Literal("Isoretikulare MOFs", lang="de")))
g.add((user["ZeoliticImidazolateFrameworks"], SKOS.prefLabel, Literal("Zeolithische Imidazolatgerüste", lang="de")))
g.add((user["MetalCarboxylateFrameworks"], SKOS.prefLabel, Literal("Metallcarboxylatgerüste", lang="de")))
g.add((user["GasStorageAndSeparation"], SKOS.prefLabel, Literal("Gasspeicherung und -trennung", lang="de")))
g.add((user["Catalysis"], SKOS.prefLabel, Literal("Katalyse", lang="de")))
g.add((user["Sensors"], SKOS.prefLabel, Literal("Sensoren", lang="de")))
g.add((user["DrugDelivery"], SKOS.prefLabel, Literal("Arzneimittelabgabe", lang="de")))

# Define properties and their characteristics
properties = {
    "metals": user["MetalCharacteristics"],
    "max_metal_coordination_n": user["MetalCharacteristics"],
    "metal_sbu_smile": user["MetalCharacteristics"],
    "metal_cluster_smile": user["MetalCharacteristics"],
    "linker_smile": user["LinkerCharacteristics"],
    "n_sbu_point_of_extension": user["LinkerCharacteristics"],
    "n_linker_point_of_extension": user["LinkerCharacteristics"],
    "ligand_smile": user["StructuralProperties"],
    "n_channel": user["StructuralProperties"],
    "void_fraction": user["PorosityMetrics"],
    "ASA_A2": user["PorosityMetrics"],
    "AV_A3": user["PorosityMetrics"],
    "pld": user["PorosityMetrics"],
    "lcd": user["PorosityMetrics"],
    "lfpd": user["PorosityMetrics"]
}

# Add properties and create hierarchy
# Add properties and create hierarchy
for prop_name, char_class in properties.items():
    # Define property as data property and its characteristic as its superclass
    g.add((prop[prop_name], RDF.type, OWL.DatatypeProperty))
    g.add((prop[prop_name], RDFS.subPropertyOf, char_class))
    # Add SKOS annotations for explanations
    if prop_name == "metals":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'metals' property refers to the characteristics related to the metal nodes in Metal-Organic Frameworks (MOFs), such as the types of metals present in the framework structure.", lang="en")))
    elif prop_name == "max_metal_coordination_n":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'max_metal_coordination_n' property represents the maximum coordination number of metal nodes in Metal-Organic Frameworks (MOFs). Coordination number refers to the number of ligands attached to a metal ion in a coordination complex.", lang="en")))
    elif prop_name == "metal_sbu_smile":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'metal_sbu_smile' property likely refers to the simplified chemical representation (SMILES notation) of the metal-containing secondary building units (SBUs) used in Metal-Organic Frameworks (MOFs). SBUs are clusters of metal ions connected by organic ligands.", lang="en")))
    elif prop_name == "metal_cluster_smile":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'metal_cluster_smile' property likely refers to the simplified chemical representation (SMILES notation) of the metal clusters used in Metal-Organic Frameworks (MOFs). These metal clusters are part of the framework structure and play a crucial role in defining the material's properties.", lang="en")))
    elif prop_name == "linker_smile":
        g.add((prop[prop_name], SKOS.definition, Literal("The term 'linker_smile' in the context of Metal-Organic Frameworks (MOFs) likely refers to the simplified chemical representation of the linker molecules used to construct the framework. SMILES (Simplified Molecular Input Line Entry System) is a notation system for representing the structure of molecules using ASCII strings. In the context of MOFs, linkers are organic molecules that connect metal nodes, forming the structural framework of the material. These linkers are often represented in databases and computational studies using SMILES notation for ease of representation and analysis. For example, a common linker used in MOFs is benzene dicarboxylate, which could be represented in SMILES notation as 'O=C(O)c1ccccc1C(=O)O'. This notation compactly represents the structure of the molecule using a string of characters, making it easy to store and process computationally.", lang="en")))
    elif prop_name == "n_sbu_point_of_extension":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'n_sbu_point_of_extension' property represents the number of extension points (functional groups) available on the metal-containing secondary building units (SBUs) in Metal-Organic Frameworks (MOFs). Extension points provide sites for attaching linker molecules, allowing for the expansion of the framework structure.", lang="en")))
    elif prop_name == "n_linker_point_of_extension":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'n_linker_point_of_extension' property represents the number of extension points (functional groups) available on the linker molecules in Metal-Organic Frameworks (MOFs). Extension points provide sites for connecting to metal-containing secondary building units (SBUs), enabling the expansion of the framework structure.", lang="en")))
    elif prop_name == "ligand_smile":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'ligand_smile' property likely refers to the simplified chemical representation (SMILES notation) of the organic ligands used in Metal-Organic Frameworks (MOFs). Ligands are organic molecules that coordinate with metal ions to form the framework structure of MOFs.", lang="en")))
    elif prop_name == "n_channel":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'n_channel' property represents the number of channels or pores present in Metal-Organic Frameworks (MOFs). These channels play a crucial role in determining the material's porosity and its potential applications in gas storage, separation, and catalysis.", lang="en")))
    elif prop_name == "void_fraction":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'void_fraction' property represents the fraction of the total volume of a Metal-Organic Framework (MOF) that is unoccupied by atoms or molecules. It is a measure of the material's porosity and is important for applications such as gas storage and separation.", lang="en")))
    elif prop_name == "ASA_A2":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'ASA_A2' property represents the accessible surface area (ASA) of a Metal-Organic Framework (MOF) per unit volume. It is a measure of the material's surface area available for interaction with molecules and is relevant for applications such as adsorption and catalysis.", lang="en")))
    elif prop_name == "AV_A3":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'AV_A3' property represents the accessible volume (AV) of a Metal-Organic Framework (MOF) per unit volume. It is a measure of the volume available for molecules to enter and interact with the framework and is important for applications such as gas storage and separation.", lang="en")))
    elif prop_name == "pld":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'pld' property represents the largest cavity diameter (PLD) within a Metal-Organic Framework (MOF). It is a measure of the size of the largest pore or channel in the framework structure and is relevant for applications such as gas adsorption and separation.", lang="en")))
    elif prop_name == "lcd":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'lcd' property represents the largest cavity diameter (LCD) within a Metal-Organic Framework (MOF) after removal of solvent molecules. It is a measure of the size of the largest pore or channel in the framework structure when the material is activated and is relevant for applications such as gas adsorption and separation.", lang="en")))
    elif prop_name == "lfpd":
        g.add((prop[prop_name], SKOS.definition, Literal("The 'lfpd' property represents the largest free pore diameter (LFPD) within a Metal-Organic Framework (MOF). It is a measure of the size of the largest pore or channel in the framework structure that is accessible to guest molecules and is relevant for applications such as gas adsorption and separation.", lang="en")))


# # Populate the graph with instances and property values
# for index, row in df.iterrows():
#     mof_node = user[row["Refcode"]]
#     g.add((mof_node, RDF.type, user["MOFMaterial"]))
#     for prop_name, value in row.items():
#         if pd.notna(value):
#             # Create a Literal for the value to ensure special characters are handled correctly
#             literal_value = Literal(value)
#             g.add((mof_node, prop[prop_name], literal_value))

# Serialize the RDF graph
g.serialize(destination='MOF.ttl', format='turtle', encoding='utf-8')
