#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dual_Adsorption_vdW/groups"
shortDesc = u""
longDesc = u"""
Two vdW species reacting together and abstracting a functional group and then forming a single bond to the surface.

*2=*3  *4-*6           *2-*3-*4     *6
  :      :     ---->    |            |
~*1~ + ~*5~~          ~*1~       + ~*5~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s).

"""

template(reactants=["Adsorbate1","Adsorbate2"], products=["Adsorbate3","Adsorbate4"], ownReverse=False)

reverse = "Surface_Dual_Desorption_vdW"

reactantNum=2
productNum=2

recipe(actions=[
    ['CHANGE_BOND','*2', -1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*4', 1, '*6'],
    ['FORM_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*5', 1, '*6'],
])

entry(
    index = 1,
    label = "Adsorbate1",
    group =
"""
multiplicity [1]
1 *1 Xv  u0 p0 c0
2 *2 R!H u0 px cx {3,[D,T,Q]}
3 *3 R!H u0 px cx {2,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Adsorbate2",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 R  u0 px cx {3,S}
3 *4 R  u0 px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "O",
    group =
"""
multiplicity [1]
1 *1 Xv  u0 p0 c0
2 *2 O   u0 px cx {3,D}
3 *3 R!H u0 px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "O=N",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u0 px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "C=O",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D}
3 *3 O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "O=C",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 C  u0 px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "RNO",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u0 p1 c0 {2,D} {4,S}
4    R  u0 px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "C$C",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,Q}
3 *3 C  u0 p0 c0 {2,Q}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "O=O",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "RONO",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u0 p1 c0 {2,D} {4,S}
4    O  u0 p2 c0 {3,S} {5,S}
5    R  u0 p0 c0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "HONO",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u0 p1 c0 {2,D} {4,S}
4    O  u0 p2 c0 {3,S} {5,S}
5    H  u0 p0 c0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "C",
    group =
"""
multiplicity [1]
1 *1 Xv  u0 p0 c0
2 *2 C   u0 px cx {3,[D,T,Q]}
3 *3 R!H u0 px cx {2,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "CO2",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D} {4,D}
3 *3 O  u0 p2 c0 {2,D}
4    O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "CC",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,[D,T,Q]}
3 *3 C  u0 p0 c0 {2,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "C=C",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D}
3 *3 C  u0 p0 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "C#C",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,T}
3 *3 C  u0 p0 c0 {2,T}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "CN",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 px cx {3,[D,T]}
3 *3 N  u0 px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "C=N",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D}
3 *3 N  u0 px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "C#N",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 px cx {3,T}
3 *3 N  u0 px cx {2,T}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "C=N-R",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D}
3 *3 N  u0 px c0 {2,D} {4,S}
4    R  u0 px c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "RC#N",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,T} {4,S}
3 *3 N  u0 p1 c0 {2,T}
4    R  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "N",
    group =
"""
multiplicity [1]
1 *1 Xv  u0 p0 c0
2 *2 N   u0 px cx {3,[D,T]}
3 *3 R!H u0 px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "N=O",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  u0 px cx {3,D}
3 *3 O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "NC",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  u0 px cx {3,[D,T]}
3 *3 C  u0 px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "N=C",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  u0 px cx {3,D}
3 *3 C  u0 px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "N#C",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  u0 px cx {3,T}
3 *3 C  u0 px cx {2,T}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "R-N=C",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 C  u0 p0 c0 {3,D}
3 *2 N  u0 px c0 {2,D} {4,S}
4    R  u0 px c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "N#CR",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 C  u0 p0 c0 {3,T} {4,S}
3 *2 N  u0 p1 c0 {2,T}
4    R  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "ONOH",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0 {3,D}
3 *2 N  u0 p1 c0 {2,D} {4,S}
4    O  u0 p2 c0 {3,S} {5,S}
5    H  u0 p0 c0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "ONOR",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0 {3,D}
3 *2 N  u0 p1 c0 {2,D} {4,S}
4    O  u0 p2 c0 {3,S} {5,S}
5    R  u0 p0 c0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "ONR",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0 {3,D}
3 *2 N  u0 p1 c0 {2,D} {4,S}
4    R  u0 px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "O-R",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 O  u0 p2 cx {3,S}
3 *4 R  u0 px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "C-R",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 C  u0 px cx {3,S}
3 *4 R  u0 px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "H-H",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 H  u0 p0 c0 {3,S}
3 *4 H  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "N-R",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 N  u0 px cx {3,S}
3 *4 R  u0 px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "O-O",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 O  u0 p2 c0 {3,S}
3 *4 O  u0 p2 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "HO-OH",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 O  u0 p2 c0 {3,S} {5,S}
3 *4 O  u0 p2 c0 {2,S} {4,S}
4    H  u0 p0 c0 {3,S}
5    H  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "O-N",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 O  u0 p2 c0 {3,S}
3 *4 N  u0 p1 c0 {2,S} {4,[S,D]}
4    R  u0 px cx {3,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "O-C",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 O  u0 p2 c0 {3,S}
3 *4 C  u0 p0 c0 {2,S} {4,[S,D,T]}
4    R  u0 px cx {3,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "O-C-3R",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 O  u0 p2 c0 {3,S}
3 *4 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4    R  u0 px cx {3,S}
5    R  u0 px cx {3,S}
6    R  u0 px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "O-C=R",
    group =
"""
multiplicity [1]
1 *5 Xv  u0 p0 c0
2 *6 O   u0 p2 c0 {3,S}
3 *4 C   u0 p0 c0 {2,S} {4,D} {5,S}
4    R!H u0 px cx {3,D}
5    R   u0 px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "O-C#R",
    group =
"""
multiplicity [1]
1 *5 Xv  u0 p0 c0
2 *6 O   u0 p2 c0 {3,S}
3 *4 C   u0 p0 c0 {2,S} {4,T}
4    R!H u0 px cx {3,T}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "O-N-2R",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 O  u0 p2 c0 {3,S}
3 *4 N  u0 p1 c0 {2,S} {4,S} {5,S}
4    R  u0 px cx {3,S}
5    R  u0 px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "O-NHH",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 O  u0 p2 c0 {3,S}
3 *4 N  u0 p1 c0 {2,S} {4,S} {5,S}
4    H  u0 p0 c0 {3,S}
5    H  u0 p0 c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "O-N=R",
    group =
"""
multiplicity [1]
1 *5 Xv  u0 p0 c0
2 *6 O   u0 p2 c0 {3,S}
3 *4 N   u0 p1 c0 {2,S} {4,D}
4    R!H u0 px cx {3,D}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "C-C",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 C  u0 px cx {3,S}
3 *4 C  u0 px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "C-O",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 C  u0 px cx {3,S}
3 *4 O  u0 p2 cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "C-N",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 C  u0 px cx {3,S}
3 *4 N  u0 p1 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "C-OH",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 C  u0 px cx {3,S}
3 *4 O  u0 p2 c0 {2,S} {4,S}
4    H  u0 p0 c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "N-N",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 N  u0 px cx {3,S}
3 *4 N  u0 px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "N-O",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 N  u0 px cx {3,S}
3 *4 O  u0 p2 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "N-C",
    group =
"""
multiplicity [1]
1 *5 Xv u0 p0 c0
2 *6 N  u0 px cx {3,S}
3 *4 C  u0 px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "O=C=O",
    group =
"""
multiplicity [1]
1    O  u0 p2 c0 {3,D}
2 *2 O  u0 p2 c0 {3,D}
3 *3 C  u0 p0 c0 {1,D} {2,D}
4 *1 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "HNO",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u0 p1 c0 {2,D} {4,S}
4    H  u0 p0 c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "2R-C=O",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0 {3,D}
3 *2 C  u0 p0 c0 {2,D} {4,S} {5,S}
4    R  u0 px cx {3,S}
5    R  u0 px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "R=C=O",
    group =
"""
multiplicity [1]
1 *1 Xv  u0 p0 c0
2 *3 O   u0 p2 c0 {3,D}
3 *2 C   u0 p0 c0 {2,D} {4,D}
4    R!H u0 px cx {3,D}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "NN",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  u0 px cx {3,[D,T]}
3 *3 N  u0 px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "N=N",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  u0 px cx {3,D}
3 *3 N  u0 px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "N2",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  u0 p1 c0 {3,T}
3 *3 N  u0 p1 c0 {2,T}
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate1
    L2: O
        L3: O=C
            L4: O=C=O
        L3: O=O
        L3: O=N
            L4: RNO
                L5: RONO
                    L6: HONO
                L5: HNO
    L2: C
        L3: C=O
            L4: 2R-C=O
            L4: R=C=O
                L5: CO2
        L3: CC
            L4: C=C
            L4: C#C
            L4: C$C
        L3: CN
            L4: C=N
                L5: C=N-R
            L4: C#N
                L5: RC#N
    L2: N
        L3: NC
            L4: N=C
                L5: R-N=C
            L4: N#C
                L5: N#CR
        L3: N=O
            L4: ONR
                L5: ONOR
                    L6: ONOH
        L3: NN
            L4: N=N
            L4: N2

L1: Adsorbate2
    L2: H-H
    L2: O-R
        L3: O-O
            L4: HO-OH
        L3: O-N
            L4: O-N-2R
                L5: O-NHH
            L4: O-N=R
        L3: O-C
            L4: O-C-3R
            L4: O-C=R
            L4: O-C#R
    L2: C-R
        L3: C-C
        L3: C-O
            L4: C-OH
        L3: C-N
    L2: N-R
        L3: N-N
        L3: N-O
        L3: N-C
"""
)

forbidden(
    label = "chargedBond",
    group =
"""
1 *2 R!H ux c[+1,-1] {2,[S,D,T]}
2 *3 R!H ux c[+1,-1] {1,[S,D,T]}
3 *1 Xv  u0 p0 c0
""",
    shortDesc = u"""""",
    longDesc =
u"""
The adsorbing molecule should not have a charge on the surface.
""",
)
