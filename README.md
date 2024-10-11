# Autókölcsönző Rendszer

Ez a projekt egy egyszerű autókölcsönző rendszert valósít meg Python használatával. A rendszer lehetővé teszi autók kölcsönzését, a bérlések nyilvántartását, valamint a meglévő bérlések lemondását.

## Követelmények

- Python 3.12.2
- Egyéb Python csomagok

## Fájlok és mappák

A projekt az alábbi főbb fájlokat tartalmazza:

- `main.py`: A belépési pont, amely elindítja az alkalmazást.
- `Teherauto.py`: A teherautó osztály definíciója.
- `Autokolcsonzo.py`: Az autókölcsönző osztály definíciója és alapértelmezett adatok betöltése.
- `Szemelyauto.py`: A személyautó osztály definíciója.
- `Auto.py`: Az autó alaposztály és az autómárkák definíciója.
- `Berles.py`: A bérlés osztály definíciója.
- `adatok.txt`: A személyes adatok fájlja.
- `test_basic.py`: A teszteseteket tartalmazó fájl.
- `Apphandler.py`: A menükezelésért felelős osztály.
- `Errorhandler.py`: A hiba kezelési dekorátor.
- `Valasztas.py`: Az egyes menüpontok enumerációja.

## Használat

### Indítási útmutató

A projekt indításához kövesse az alábbi lépéseket:

1. Klónozza a repozitorit a helyi gépére.
2. Navigáljon a projekt gyökérkönyvtárába.
3. Futtassa a következő parancsot a fő szkript indításához:
   ```bash
   python main.py
   ```
   vagy
   ```bash
   py main.py
   ```

### Funkcionalitás

A rendszer a következő főbb funkciókat támogatja:

#### Menü Megjelenítése

Az `AppHandler` osztály tartalmazza a `print_menu` metódust, amely megjeleníti az autókölcsönző rendszer menüjét.

#### Menüinput Konvertálása

Az `AppHandler` osztály tartalmazza a `convert_menu_input` metódust, amely konvertálja a felhasználó bevitt menüpontját megfelelő választási lehetőséggé.

#### Adatok Bekérése a Bemenetről

Az `AppHandler` osztály tartalmazza a `get_data_from_input` metódust, amely bekéri az autó rendszámát és a bérlés dátumát a felhasználótól.

#### Autók Bérlése

Az `AppHandler` osztály `berles` metódusa lehetővé teszi az autók bérlését egy adott dátumra. Ha sikeres, akkor kiírja a bérlés árát, ellenkező esetben tájékoztatást ad az elérhetőségről.

#### Bérlés Lemondása

Az `AppHandler` osztály `lemondas` metódusa lehetővé teszi a meglévő bérlés lemondását. Sikeres lemondás esetén visszaigazolást nyújt, ellenkező esetben tájékoztatja a felhasználót a hiba okáról.

#### Listázás

Az `AppHandler` osztály `listazas` metódusa listázza az autókat vagy a bérléseket, aszerint, hogy milyen paraméterrel hívjuk meg.

## Hibakezelés

A rendszer egy dekorátor (`catch_all_exceptions`) segítségével kezeli az összes metódusban bekövetkező összes kivételt. Minden kivételnél az alkalmazás újraindul, hogy a felhasználó ismét megpróbálhassa a műveletet.

## Adatok

A projekt tartalmaz egy `adatok.txt` fájlt, amelyben a személyes adatok vannak (név, neptunkód, szak)

## Tesztelés
A projekt tartalmaz egy `test_basic.py` fájlt, amely az összes fő funkcionalitást teszteli. A tesztek használatához futtassa az alábbi parancsot a projekt gyökérkönyvtárából:

```bash
   pytest
   ```

### Tesztelt Funkciók
- Autók bérlése (`berles`): A teszt szimulálja az autóbérlést, és ellenőrzi, hogy a várt üzenet megjelenik-e.
- Bérlés lemondása (`lemondas`): A teszt szimulálja a bérlés lemondását, és ellenőrzi, hogy a várt üzenet megjelenik-e.
- Kilépés (`kilepes`): A teszt szimulálja az alkalmazásból való kilépést, és ellenőrzi, hogy a megfelelő üzenet megjelenik-e, valamint hogy a rendszer valóban kilép.
- Menü megjelenítése (`print_menu`): A teszt ellenőrzi, hogy a menü helyesen jelenik meg.
- Bérlések listázása (`listazas`): A teszt ellenőrzi, hogy a bérlések helyesen kerülnek listázásra.
- Autók listázása (`listazas`, `True` paraméterrel): A teszt ellenőrzi, hogy az autók helyesen kerülnek listázásra.