from SSBU26.cv5.code.data_handling import Dataset


# ulohy
# 1
dataset = Dataset()
statistiky = dataset.calculate_statistics()
print(statistiky)


#2
X_train, X_test, y_train, y_test = dataset.split_data()

X_train_std, X_test_std = dataset.scale_data(X_train, X_test, scale_type='standard')
X_train_norm, X_test_norm = dataset.scale_data(X_train, X_test, scale_type='normalize')
X_train_rob, X_test_rob = dataset.scale_data(X_train, X_test, scale_type='robust')

dataset.plot_all_features_before_after_scaling(X_train, X_train_std, 'standard')
dataset.plot_all_features_before_after_scaling(X_train, X_train_norm, 'normalize')
dataset.plot_all_features_before_after_scaling(X_train, X_train_rob, 'robust')


# 3
summary = dataset.summarize_features()
print("\n 3. Uloha zhrnutie vlastnosti:")
print(summary)

# 4
vybrane_vlastnosti = ['mean radius', 'area error', 'worst concavity']
zhrnutie_vybranych = dataset.summarize_features(feature_names=vybrane_vlastnosti)

print("\n 4. Uloha - vybrane vlastnosti:")
print(zhrnutie_vybranych)

#5
dataset.plot_correlation_matrix()
dataset.feature_importance()
dataset.plot_box_plots(scaled_data=X_train_std, target=y_train)


#********************************** DOKUMENTACIA *******************************************
# Z korelacnej matice najviac pozitivne koreluju mean radius a mean perimeter. Potom mean radius a mean area
# Negativne to su - mean radius a mean fractal dimension a mean area a mean fractal dimension
#
# stlpcovy graf Feature Importances,
# model sa nespolieha na vsetky data rovnomerne.
# Prve tri premenne dominuju celemu grafu
# najvyssia dosahuje hodnotu skoro 0.14
# vlastnosti na pravej strane grafu klesaju takmer k nule a pre model su zrejme minimalne podstatne.

# box plot
# rozdeleny podla cielovej triedy target 0 a 1
# Modre a oranzove boxy su pri niektorych stlpcoch napr. mean concavity alebo worst area
# vyskovo posunute od seba a takmer sa neprekryvaju, takze sa daju velmi dobre vizualne odlisit.
# pri stlpcoch ako smoothness error alebo symmetry error su boxy takmer v rovnakej vyske,
# cize na oddelenie tried velmi nepomozu

# 2 Vplyv metod skalovania na dataset:
# Pri neskalovanych datach je vidiet obrovsky nepomer v mierkach

# Standardizacia
# vsetky boxploty sa vizualne zjednotili a mediany sa posunuli skoro na uroven nuly.
# Hodnoty na x osi sa teraz pohybuju zhruba od -2 do 12.

# Normalizacia
# najvacsia zmena osi x. Vsetky data su na intervale od 0 do 1

# Robustne
# mediany su sice zarovnane na 0, ale os x ide az takmer k 20.
# Pri vlastnostiach ako area error su extremne odchylky ovela viditelnejsie ako pri klasickej standardizacii


