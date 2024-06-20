Můj první projekt

Co by jsi měl/a zlepšit: Co zlepšit:
1. Statistika slov, které začínají velkým písmem: zde výpis ['Situated', 'Kemmerer', 'Fossil', 'Butte', 'Twin', 'Creek', 'Valley', 'The', '30N', 'Union', 'Pacific', 'Railroad'] - pozor na metodu istitle, ta evokuje k tomu, že zjistí zda slovo začíná velkým písmenem, což je částečně pravda. Ale istitle funguje následovně, zjistí zda první abecední znak ve slově je velký a ostatní malé, ale ignoruje neabecední znaky. Takže istitle vidí slovo 30N jako N. Zkus si pohrát s metodou isupper, isaplha a istitle a koukej jak se chovají v různých situacích


Opraveno za použití metody .isupper snad už to bude ok 
