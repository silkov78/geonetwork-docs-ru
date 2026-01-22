# Рэжым аўтэнтыфікацыі

Па змаўчанні каталог выкарыстоўвае ўнутраную базу даных для кіравання карыстальнікамі і аўтэнтыфікацыі. Аднак існуюць і іншыя механізмы аўтэнтыфікацыі:

- [Наладка LDAP](authentication-mode.md#authentication-ldap)
- [Наладка LDAP - Іерархія](authentication-mode.md#authentication-ldap-hierarchy)
- [Наладка CAS](authentication-mode.md#authentication-cas)
- [Наладка OAUTH2 OpenID Connect](authentication-mode.md#authentication-openid)
- [Наладка Keycloak](authentication-mode.md#authentication-keycloak)
- [Наладка Shibboleth](authentication-mode.md#authentication-shibboleth)

Выкарыстоўваемы рэжым наладжваецца ў **`WEB-INF/config-security/config-security.xml`** або праз зменную асяроддзя `geonetwork.security.type`.

Раскаментуйце адпаведны радок у **`WEB-INF/config-security/config-security.xml`**:

```xml
<import resource="config-security-{mode}.xml"/>
```

## Наладка LDAP {#authentication-ldap}

[Палегчаны пратакол доступу да каталогаў (LDAP)](https://en.wikipedia.org/wiki/Ldap) дазваляе GeoNetwork правяраць імёны карыстальнікаў і паролі ў аддаленым сховішчы ідэнтыфікацыйных даных. Рэалізацыя LDAP выкарыстоўвае стандартныя элементы інтэрфейсу ўваходу GeoNetwork.

У GeoNetwork ёсць 2 падыходы да наладкі LDAP. Праверце таксама альтэрнатыўны падыход у [Наладка LDAP - Іерархія](authentication-mode.md#authentication-ldap-hierarchy).

Канфігурацыя LDAP вызначана ў `WEB-INF/config-security/config-security.properties`. Вы можаце наладзіць асяроддзе, абнавіўшы гэты файл або перавызначыўшы ўласцівасці ў файле `WEB-INF/config-security/config-security-overrides.properties`.

1. Вызначыце падключэнне LDAP:

    - `ldap.base.provider.url`: Указвае парталу, дзе знаходзіцца сервер LDAP. Пераканайцеся, што камп'ютар з каталогам можа падключыцца да камп'ютара з серверам LDAP. Праверце, ці адкрыты адпаведныя парты і г.д.
    - `ldap.base.dn`: звычайна гэта выглядае прыкладна так: "dc=[organizationnamehere],dc=org"
    - `ldap.security.principal` / `ldap.security.credentials`: Вызначыце карыстальніка адміністратара LDAP для прывязкі да LDAP. Калі не вызначана, выконваецца ананімная прывязка. Principal - гэта імя карыстальніка, а credentials - пароль.

    ```text
    # Уласцівасці бяспекі LDAP
    ldap.base.provider.url=ldap://localhost:389
    ldap.base.dn=dc=fao,dc=org
    ldap.security.principal=cn=admin,dc=fao,dc=org
    ldap.security.credentials=ldap
    ```

    Каб праверыць правільнасць наладак, паспрабуйце падключыцца да сервера LDAP з дапамогай браўзера LDAP.

2. Вызначыце, дзе шукаць карыстальнікаў у структуры LDAP для аўтэнтыфікацыі:

    - `ldap.base.search.base`: тут каталог будзе шукаць карыстальнікаў для аўтэнтыфікацыі.
    - `ldap.base.dn.pattern`: гэта адметнае імя карыстальніка для прывязкі. `{0}` замяняецца імем карыстальніка, уведзеным на экране ўваходу.

    ```text
    ldap.base.search.base=ou=people
    ldap.base.dn.pattern=uid={0},${ldap.base.search.base}
    #ldap.base.dn.pattern=mail={0},${ldap.base.search.base}
    ```

### Наладкі аўтарызацыі

Пры выкарыстанні LDAP інфармацыя пра карыстальніка і прывілеі для GeoNetwork могуць быць вызначаны з атрыбутаў LDAP.

#### Інфармацыя пра карыстальніка

Інфармацыя пра карыстальніка можа быць атрымана з LDAP, наладзіўшы для кожнага атрыбута карыстальніка ў базе даных каталога адпаведны атрыбут LDAP. Калі атрыбут пусты або не вызначаны, можна задаць значэнне па змаўчанні. Значэнне ўласцівасці складаецца з дзвюх частак, падзеленых сімвалам `,`. Першая частка - гэта імя атрыбута, а другая - значэнне па змаўчанні, калі імя атрыбута не вызначана або значэнне атрыбута ў LDAP пустое.

Канфігурацыя наступная:

```text
# Супастаўленне інфармацыі пра карыстальніка з атрыбутамі LDAP і значэннямі па змаўчанні
# ldapUserContextMapper.mapping[name]=ldap_attribute,default_value
ldapUserContextMapper.mapping[name]=cn,
ldapUserContextMapper.mapping[surname]=givenName,
ldapUserContextMapper.mapping[mail]=mail,data@myorganization.org
ldapUserContextMapper.mapping[organisation]=,myorganization
ldapUserContextMapper.mapping[kind]=,
ldapUserContextMapper.mapping[address]=,
ldapUserContextMapper.mapping[zip]=,
ldapUserContextMapper.mapping[state]=,
ldapUserContextMapper.mapping[city]=,
ldapUserContextMapper.mapping[country]=,
```

#### Канфігурацыя прывілеяў

Групы карыстальнікаў і профілі карыстальнікаў могуць быць устаноўлены апцыянальна з інфармацыі LDAP ці не. Па змаўчанні прывілеі карыстальнікаў кіруюцца з лакальнай базы даных. Калі інфармацыя LDAP павінна выкарыстоўвацца для вызначэння прывілеяў карыстальнікаў, усталюйце ўласцівасць `ldap.privilege.import` у `true`:

```text
ldap.privilege.import=true
```

Пры імпарце прывілеяў з LDAP адміністратар каталога можа вырашыць ствараць групы, вызначаныя ў LDAP і не вызначаныя ў лакальнай базе даных. Для гэтага усталюйце наступную ўласцівасць у true:

```text
ldap.privilege.create.nonexisting.groups=false
```

Каб вызначыць, членам якіх груп з'яўляецца карыстальнік і які профіль мае карыстальнік:

```text
ldapUserContextMapper.mapping[privilege]=groups,sample
# Калі не ўстаноўлена, профіль па змаўчанні - RegisteredUser
# Дапушчальныя профілі: ADMINISTRATOR, USER_ADMIN, REVIEWER, EDITOR, REGISTERED_USER, GUEST
ldapUserContextMapper.mapping[profile]=privileges,RegisteredUser
```

Канфігурацыя атрыбутаў:

- атрыбут privilege змяшчае групу, членам якой з'яўляецца гэты карыстальнік. Дапускаецца больш за адну групу.
- атрыбут profile змяшчае профіль карыстальніка.

Дапушчальныя профілі карыстальнікаў:

- Administrator
- UserAdmin
- Reviewer
- Editor
- RegisteredUser
- Guest

Калі атрыбут LDAP, які змяшчае профілі, не адпавядае спісу профіляў каталога, можна вызначыць супастаўленне:

```text
# Супастаўленне карыстальніцкіх профіляў LDAP з профілямі каталога. Не выкарыстоўваецца, калі вызначаны ldap.privilege.pattern.
ldapUserContextMapper.profileMapping[Admin]=Administrator
ldapUserContextMapper.profileMapping[Editor]=Reviewer
ldapUserContextMapper.profileMapping[Public]=RegisteredUser
```

Напрыклад, у папярэдняй канфігурацыі значэнне атрыбута `Admin` будзе супастаўлена з `Administrator` (які з'яўляецца дапушчальным профілем для каталога).

Атрыбут можа вызначаць як профіль, так і групу для карыстальніка. Каб выняць гэтую інфармацыю, можна вызначыць карыстальніцкі шаблон для запаўнення прывілеяў карыстальніка ў адпаведнасці з гэтым атрыбутам:

1. Вызначыце адзін атрыбут для профілю і адзін для груп у `WEB-INF/config-security/config-security-overrides.properties`

    ```text
    # У config-security-overrides.properties
    ldapUserContextMapper.mapping[privilege]=cat_privileges,sample
    ```

2. Вызначыце адзін атрыбут для прывілеі і вызначыце карыстальніцкі шаблон:

    ```text
    # У config-security.properties
    ldap.privilege.pattern=CAT_(.*)_(.*)
    ldap.privilege.pattern.idx.group=1
    ldap.privilege.pattern.idx.profil=2
    ```

    Уключыце бін `er` для `LDAPUserDetailsContextMapperWithPattern` (у `WEB-INF/config-security/config-security-ldap.xml`).

    ```xml
    <!--<bean id="ldapUserContextMapper"
        class="org.fao.geonet.kernel.security.ldap.LDAPUserDetailsContextMapper">
        <property name="mapping">
          <map/>
        </property>
        <property name="profileMapping">
          <map/>
        </property>
        <property name="ldapBaseDn" value="${ldap.base.dn}"/>
        <property name="importPrivilegesFromLdap" value="${ldap.privilege.import}"/>
        <property name="createNonExistingLdapGroup"
                  value="${ldap.privilege.create.nonexisting.groups}"/>
        <property name="createNonExistingLdapUser" value="${ldap.privilege.create.nonexisting.users}"/>
        <property name="ldapManager" ref="ldapUserDetailsService"/>
        <property name="contextSource" ref="contextSource"/>
        <property name="ldapUsernameCaseInsensitive" value="${ldap.usernameCaseInsensitive:#{true}}"/>
    </bean>-->

    <bean id="ldapUserContextMapper" class="org.fao.geonet.kernel.security.ldap.LDAPUserDetailsContextMapperWithPattern">
      <property name="mapping">
          <map/>
      </property>
      <property name="profileMapping">
          <map/>
      </property>
      <property name="importPrivilegesFromLdap" value="${ldap.privilege.import}"/>
      <property name="createNonExistingLdapGroup" value="${ldap.privilege.create.nonexisting.groups}" />
      <property name="createNonExistingLdapUser" value="${ldap.privilege.create.nonexisting.users}" />

      <property name="ldapManager" ref="ldapUserDetailsService" />

      <property name="privilegePattern" value="${ldap.privilege.pattern}" />
      <property name="groupIndexInPattern" value="${ldap.privilege.pattern.idx.group}"/>
      <property name="profilIndexInPattern" value="${ldap.privilege.pattern.idx.profil}"/>

      <property name="contextSource" ref="contextSource" />
    </bean>
    ```

3. Вызначыце карыстальніцкае месцазнаходжанне для вымання групы і ролі (няма падтрымкі камбінацыі група/роля) (выкарыстоўвайце LDAPUserDetailsContextMapperWithProfileSearch у **`config-security.xml`**).

    ```text
    ldap.privilege.search.group.attribute=cn
    ldap.privilege.search.group.object=ou=groups
    #ldap.privilege.search.group.query=(&(objectClass=*)(memberUid=uid={0},${ldap.base.search.base},${ldap.base.dn})(cn=EL_*))
    ldap.privilege.search.group.queryprop=memberuid
    ldap.privilege.search.group.query=(&(objectClass=*)(memberUid=uid={0},${ldap.base.search.base},${ldap.base.dn})(|(cn=SP_*)(cn=EL_*)))
    ldap.privilege.search.group.pattern=EL_(.*)
    ldap.privilege.search.privilege.attribute=cn
    ldap.privilege.search.privilege.object=ou=groups
    ldap.privilege.search.privilege.query=(&(objectClass=*)(memberUid=uid={0},${ldap.base.search.base},${ldap.base.dn})(cn=SV_*))
    ldap.privilege.search.privilege.pattern=SV_(.*)
    ```

    Атрыбут LDAP можа змяшчаць наступную канфігурацыю для вызначэння розных тыпаў карыстальнікаў, напрыклад:

    ```text
    cat_privileges=CAT_ALL_Administrator

    -- Вызначыць рэцэнзента для групы GRANULAT
    cat_privileges=CAT_GRANULAT_Reviewer

    -- Вызначыць рэцэнзента для групы GRANULAT і рэдактара для MIMEL
    cat_privileges=CAT_GRANULAT_Reviewer
    cat_privileges=CAT_MIMEL_Editor

    -- Вызначыць рэцэнзента для групы GRANULAT і рэдактара для MIMEL і RegisteredUser для NATURA2000
    cat_privileges=CAT_GRANULAT_Reviewer
    cat_privileges=CAT_MIMEL_Reviewer
    cat_privileges=CAT_NATURA2000_RegisteredUser

    -- Толькі зарэгістраваны карыстальнік для GRANULAT
    cat_privileges=CAT_GRANULAT_RegisteredUser
    ```

#### Сінхранізацыя

Задача сінхранізацыі клапоціцца пра выдаленне карыстальнікаў LDAP, якія могуць быць выдалены. Напрыклад:

- T0: Карыстальнік А ўваходзіць у каталог. Лакальны карыстальнік А ствараецца ў базе даных карыстальнікаў.
- T1: Карыстальнік А выдаляецца з LDAP (Карыстальнік А больш не можа ўвайсці ў каталог).
- T2: Задача сінхранізацыі праверыць, што ўсе лакальныя карыстальнікі LDAP існуюць у LDAP:
    - Калі карыстальнік не валодае ніякімі запісамі, ён будзе выдалены.
    - Калі карыстальнік валодае запісамі метаданых, у сістэму лагіравання каталога будзе запісана папераджальнае паведамленне. Уладальнік запісу павінен быць зменены на іншага карыстальніка, перш чым задача зможа выдаліць бягучага ўладальніка.

Па змаўчанні задача выконваецца адзін раз у дзень. Гэта можна змяніць у наступнай уласцівасці:

```text
# Запускаць сінхранізацыю LDAP кожны дзень у 23:30
ldap.sync.cron=0 30 23 * * ?
```

Наступныя ўласцівасці дазваляюць выканаць пашыраную наладку працэсу сінхранізацыі:

```text
ldap.sync.user.search.base=${ldap.base.search.base}
ldap.sync.user.search.filter=(&(objectClass=*)(mail=*@*)(givenName=*))
ldap.sync.user.search.attribute=uid
ldap.sync.group.search.base=ou=groups
ldap.sync.group.search.filter=(&(objectClass=posixGroup)(cn=EL_*))
ldap.sync.group.search.attribute=cn
ldap.sync.group.search.pattern=EL_(.*)
```

#### Адладка

Калі падключэнне не ўдаецца, паспрабуйце павялічыць узровень лагіравання для LDAP у `WEB-INF/classes/log4j.xml`:

```xml
<logger name="geonetwork.ldap" additivity="false">
    <level value="DEBUG"/>
</logger>
```

Або ў наладках канфігурацыі часова ўсталюйце `Log level` на `DEV`:

![](img/setting-log-level.png)

## Наладка LDAP - Іерархія {#authentication-ldap-hierarchy}

Некалькі іншы метад наладкі LDAP быў уведзены ў сярэдзіне 2020 года.

Ён пашырае зыходную інфраструктуру канфігурацыі (зыходныя канфігурацыі па-ранейшаму працуюць без змен).

Перад пачаткам наладкі вам спатрэбіцца ведаць:

1. URL вашага сервера LDAP
2. Імя карыстальніка/пароль для ўваходу на сервер LDAP (для выканання запытаў)
3. Запыт LDAP для пошуку карыстальніка (улічваючы тое, што яны ўводзяць на экране ўваходу)
4. Падрабязнасці пра тое, як пераўтварыць атрыбуты карыстальніка LDAP у атрыбуты карыстальніка GeoNetwork
5. Запыт LDAP для пошуку груп, членам якіх з'яўляецца карыстальнік
6. Як пераўтварыць групу LDAP у групу/профіль GeoNetwork

!!! note

    Існуе [відэачат распрацоўшчыкаў]( у якім падрабязна распавядаецца, як наладзіць LDAP, уключаючы наладку папярэдне сканфігураванага сервера LDAP (з выкарыстаннем Apache Directory Studio) для тэсціравання/адладкі/навучання.

!!! note

    Ці варта выкарыстоўваць іерархічную або зыходную канфігурацыю?

    Калі ў вас ужо ёсць існуючая (зыходная) канфігурацыя, няма неабходнасці пераходзіць на новую. Большая частка кода паміж імі аднолькавая.

    Калі вы пачынаеце новую канфігурацыю, я б рэкамендаваў іерархічную канфігурацыю. Яна крыху прасцейшая і падтрымліваецца тэставымі прыкладамі і інфраструктурай тэсціравання. Яна таксама падтрымлівае LDAP, дзе карыстальнікі/групы знаходзяцца ў некалькіх каталогах.

### Наладка бінаў LDAP (Іерархія)

GeoNetwork пастаўляецца з прыкладам канфігурацыі LDAP, які вы можаце выкарыстоўваць у Apache Directory Studio для стварэння таго ж сервера LDAP, які выкарыстоўваецца ў тэставых прыкладах. Таксама ёсць прыклад канфігурацыі GeoNetwork, якая падключаецца да гэтага сервера LDAP. Гл. `core-geonetwork/blob/master/core/src/test/resources/org/fao/geonet/kernel/security/ldap/README.md`{.interpreted-text role="repo"} або [відэачат распрацоўшчыкаў]( для інструкцый.

!!! note

    Каб выкарыстоўваць гэтую канфігурацыю, раскаментуйце радок "<import resource="config-security-ldap-recursive.xml"/>" у ``web/src/main/webapp/WEB-INF/config-security/config-security.xml``

1. Наладзьце бін `ce` са спасылкай на ваш сервер LDAP і карыстальніка, які можа выконваць запыты LDAP.

    ```xml
    <bean id="contextSource"   class="org.springframework.security.ldap.DefaultSpringSecurityContextSource">
        <constructor-arg value=“ldap://localhost:3333/dc=example,dc=com"/>

        <property name="userDn" value="cn=admin,ou=GIS Department,ou=Corporate Users,dc=example,dc=com"/>
        <property name="password" value="admin1"/>
    </bean>
    ```

2. Наладзьце бін `ch` з запытам, выкарыстоўваемым для пошуку карыстальніка (улічваючы тое, што было ўведзена на старонцы ўваходу).

    ЗАЎВАГА: Усталюйце `ee` у `ue` для выканання рэкурсіўнага пошуку ў LDAP. Выкарыстоўвайце `se` для кіравання тым, у якім каталогу пачынаецца пошук ("" азначае пачатак з кораня).

    ```xml
    <bean id="ldapUserSearch" class="…">
       <constructor-arg name="searchBase" value=""/>
       <constructor-arg name="searchFilter" value="(sAMAccountName={0})"/>
       <constructor-arg name="contextSource" ref="contextSource"/>

       <property name="searchSubtree" value="true"/>
    </bean>
    ```

3. Наладзьце бін `er` з тым, як пераўтварыць атрыбуты карыстальніка LDAP у атрыбуты карыстальніка GeoNetwork (гл. дакументацыю па зыходнай канфігурацыі вышэй).

    ЗАЎВАГА: Частка `ue` складаецца з дзвюх частак. Першая частка — гэта імя атрыбута LDAP (можа быць пустой). Другая частка — значэнне па змаўчанні, калі атрыбут LDAP адсутнічае або пусты (гл. дакументацыю па зыходнай канфігурацыі вышэй).

    ```xml
    <bean id="ldapUserContextMapper" class=“LDAPUserDetailsContextMapperWithProfileSearchEnhanced">

        <property name="mapping">
          <map>
            <entry key="name" value="cn,"/>
            <entry key="surname" value="sn,"/>
            <entry key="mail" value="mail,"/>
            <entry key="organisation" value=","/>
            <entry key="address" value=","/>
            <entry key="zip" value=","/>
            <entry key="state" value=","/>
            <entry key="city" value=","/>
            <entry key="country" value=","/>

            <entry key="profile" value=",RegisteredUser"/>
            <entry key="privilege" value=",none"/>
          </map>
        </property>

    </bean>
    ```

4. Працягніце наладку біна `er`, каб LDAP таксама мог прадастаўляць ролі груп/профіляў для карыстальніка.

    ЗАЎВАГА: `ry` — гэта каталог LDAP, у якім пачнецца запыт членства ("" азначае пачатак у корані LDAP).

    ```xml
    <bean id="ldapUserContextMapper" class="LDAPUserDetailsContextMapperWithProfileSearchEnhanced">

        <property name="importPrivilegesFromLdap" value=“true"/>

        <!-- звычайна мы не хочам, каб GN змяняў сервер LDAP! -->
        <property name="createNonExistingLdapGroup" value="false" />
        <property name="createNonExistingLdapUser" value="false" />
        <property name="ldapManager" ref="ldapUserDetailsService" />

        <property name="membershipSearchStartObject" value=""/>
        <property name="ldapMembershipQuery" value="(&amp;(objectClass=*)(member=cn={2})(cn=GCAT_*))"/>

    </bean>
    ```

5. Працягніце наладку біна `er`, каб ролі LDAP можна было пераўтварыць у групы/профілі GeoNetwork.

    ЗАЎВАГА: Вы можаце выкарыстоўваць некалькі `rs`.

    ```xml
    <bean id="ldapUserContextMapper" class="LDAPUserDetailsContextMapperWithProfileSearchEnhanced">

       <property name="ldapRoleConverters">
         <util:list>
           <ref bean="ldapRoleConverterGroupNameParser"/>
         </util:list>
       </property>

    </bean>
    ```

У цяперашні час існуе два спосабы пераўтварэння групы LDAP у групы/профілі GeoNetwork.

- `er`, які працуе гэтак жа, як зыходная канфігурацыя LDAP. Ён выкарыстоўвае рэгулярны выраз для разбору імя групы LDAP у групу/профіль GeoNetwork. Гэта пераўтворыць ролю LDAP `OR` у групу GeoNetwork `AL` з профілем `r.`

    ```xml
    <bean id="ldapRoleConverterGroupNameParser"  class="LDAPRoleConverterGroupNameParser">

        <property name="ldapMembershipQueryParser" value="GCAT_(.*)_(.*)"/>
        <property name="groupIndexInPattern" value="1"/>
        <property name="profileIndexInPattern" value=“2"/>

        <property name="profileMapping">
          <map>
            <entry key="ADMIN" value="Administrator"/>
            <entry key="EDITOR" value="Editor"/>
          </map>
        </property>

    </bean>
    ```

- Існуе таксама больш прамы спосаб з выкарыстаннем `er`. Гэта напрамую пераўтворыць імя групы LDAP у спіс груп/профіляў GeoNetwork.

    ```xml
    <bean id=“ldapRoleConverterGroupNameParser" class="LDAPRoleConverterGroupNameConverter">

        <property name="convertMap">
          <map>

            <entry>
                <key>
                    <value>HGIS_GeoNetwork_Admin</value>
                </key>
                <list>

                    <bean class="org.fao.geonet.kernel.security.ldap.LDAPRole">
                      <constructor-arg name="groupName" type="java.lang.String" value="myGroup"/>
                      <constructor-arg name="profileName" type="java.lang.String" value="Administrator"/>
                    </bean>

                </list>
            </entry>
            <entry>
              <key>
                    <value>HGIS_GeoNetwork_Editor</value>
              </key>
              <list>

                <bean class="org.fao.geonet.kernel.security.ldap.LDAPRole">
                  <constructor-arg name="groupName" type="java.lang.String" value=“myGroup"/>
                  <constructor-arg name="profileName" type="java.lang.String" value="Editor"/>
                </bean>

              </list>
            </entry>
          </map>
        </property>
    </bean>
    ```

## Наладка CAS {#authentication-cas}

Каб уключыць CAS, наладзьце аўтэнтыфікацыю, уключыўшы `WEB-INF/config-security/config-security-cas.xml` у `WEB-INF/config-security/config-security.xml`, раскаментаваўшы наступныя радкі:

```xml
<import resource="config-security-cas.xml"/>
<import resource="config-security-cas-ldap.xml"/>
```

CAS можа выкарыстоўваць альбо LDAP, альбо базу даных для кіравання карыстальнікамі. Каб выкарыстоўваць базу даных, замест гэтага раскаментуйце наступныя радкі:

```xml
<import resource="config-security-cas.xml"/>
<import resource="config-security-cas-database.xml"/>
```

Канфігурацыя CAS вызначана ў `WEB-INF/config-security/config-security.properties`. Вы можаце наладзіць сваё асяроддзе, абнавіўшы папярэдні файл або вызначыўшы перавызначэнні ўласцівасцей у файле `WEB-INF/config-security/config-security-overrides.properties`:

```text
cas.baseURL=https://localhost:8443/cas
cas.ticket.validator.url=${cas.baseURL}
cas.login.url=${cas.baseURL}/login
cas.logout.url=${cas.baseURL}/logout?url=${geonetwork.https.url}/
```

## Наладка OAUTH2 OpenID Connect {#authentication-openid}

[OAUTH2 OpenID Connect](https://openid.net/connect/) — гэта сістэма аўтэнтыфікацыі і аўтарызацыі, заснаваная на OAUTH2. Плагін OpenID Connect для Geonetwork быў пратэставаны з [Keycloak](https://keycloak.org) і [Azure AD](https://azure.microsoft.com/en-ca/services/active-directory/), але павінен працаваць з любым правайдэрам.

Асноўныя крокі наладкі:

1. Наладзьце ваш сервер IDP (напрыклад, Keycloak або Azure AD)
    1. Пераканайцеся, што токен ID прадастаўляе інфармацыю пра ролю/групу
    2. Аўтарызуйце вашы URL Geonetwork для перанакіравання (напрыклад, `http://localhost:8080/geonetwork/login/oauth2/code/geonetwork-oicd`)
    3. Запішыце Client ID
    4. Запішыце Client Secret
    5. Атрымайце JSON-дакумент метаданых сервера
2. Наладзьце Geonetwork праз зменныя асяроддзя
    1. ``GEONETWORK_SECURITY_TYPE=openidconnect``
    2. ``OPENIDCONNECT_CLIENTSECRET=\...`` (з вашага сервера IDP)
    3. ``OPENIDCONNECT_CLIENTID=\...`` (з вашага сервера IDP)
    4. ``OPENIDCONNECT_SERVERMETADATA_JSON_TEXT='\...'`` (тэкст JSON-дакумента метаданых вашага сервера)
    5. ``OPENIDCONNECT_IDTOKENROLELOCATION=\...`` (размяшчэнне роляў карыстальніка ў токене ID)

У плагіна Open ID Connect для Geonetwork шмат опцый канфігурацыі — калі ласка, гл. файлы `WEB-INF/config-security/config-security-openidconnect.xml` і `WEB-INF/config-security/config-security-openidconnect-overrides.properties`.

### Зменныя асяроддзя і іх значэнне

**GEONETWORK_SECURITY_TYPE**

Павінна быць `ct`.

**OPENIDCONNECT_CLIENTID**

Імя кліента/прыкладання, якое вы наладзілі на сваім серверы OpenID.

**OPENIDCONNECT_CLIENTSECRET**

`et`, які вы наладзілі на сваім серверы OpenID.

**OPENIDCONNECT_SERVERMETADATA_CONFIG_URL**

URL да JSON-дакумента метаданых знешняга сервера OIDC. Звычайна гэта ``/.well-known/openid-configuration`` на серверы IDP.

!!! note

    Гэта будзе загружаць канфігурацыю сервера кожны раз пры запуску GeoNetwork, што можа быць праблемай бяспекі. Для бяспекі выкарыстоўвайце URL `ps`.

**OPENIDCONNECT_SERVERMETADATA_JSON_TEXT**

Павінен быць тэкстам канфігурацыі метаданых вашага сервера OpenID (JSON).

**OPENIDCONNECT_SERVERMETADATA_FNAME**

Замест таго, каб змяшчаць канфігурацыю метаданых сервера OpenID у выглядзе тэксту ў зменную (``OPENIDCONNECT_SERVERMETADATA_JSON_TEXT``), вы можаце змясціць змесціва JSON у файл і спасылацца на яго з дапамогай гэтай зменнай (напрыклад, `/WEB-INF/config-security/openid-configuration.json`)

**OPENIDCONNECT_IDTOKENROLELOCATION**

Дзе ў токене ID захоўваюцца ролі/групы карыстальнікаў (напрыклад, "groups", "roles" або "resource_access.gn-key.roles")

**OPENIDCONNECT_ROLECONVERTER**

Гэта забяспечвае простае пераўтварэнне роляў з сервера OpenID у ролі Geonetwork.

напрыклад, ``"GeonetworkAdmin=Administrator,GeonetworkEditor=Editor"``

Гэта пераўтворыць "GeonetworkAdmin" (з сервера OpenID) у ролю "Administrator" Geonetwork.

!!! note

    Як і ў плагіне keycloak, вы можаце выкарыстоўваць імёны роляў/груп віду "group:role", каб прызначыць карыстальніка ў групу Geonetwork і ўзровень дазволаў.

**OPENIDCONNECT_MINIMUMPROFILE**

Кожнаму карыстальніку, які аўтэнтыфікуецца на серверы OpenID, будзе прысвоена гэтая роля.

Па змаўчанні ``"RegisteredUser"``.

**OPENIDCONNECT_USERPROFILEUPDATEENABLED**

Пры ўваходзе карыстальніка абнаўляць яго профіль Geotwork з токена ID сервера OpenID.

Па змаўчанні ``"true"``.

**OPENIDCONNECT_USERGROUPUPDATEENABLED**

Пры ўваходзе карыстальніка абнаўляць яго дазволы групы/ролі Geotwork.

Па змаўчанні ``"true"``.

**OPENIDCONNECT_SCOPES**

Абмежаваць вобласць доступу, якая запытваецца да сервера OpenID.

Па змаўчанні "openid email profile" і "openid email profile offline_access" (для токенаў bearer).

**OPENIDCONNECT_LOGINTYPE**

Як Geonetwork паступае з карыстальнікамі, якія не ўвайшлі ў сістэму.

Па змаўчанні "LINK" - карыстальнікі могуць націснуць на спасылку "ўвайсці" на галоўнай старонцы.

"AUTOLOGIN" - Форма ўваходу не прадастаўляецца, карыстальнік будзе аўтаматычна ўваходзіць у сістэму, калі гэта магчыма.

**OPENIDCONNECT_LOGSENSITIVE_INFO**

"true" або "false" (па змаўчанні)

Лагіруе: КОД, ТОКЕН ДОСТУПУ, ТОКЕН ID, вынік канцавой кропкі userinfo і вылічаныя паўнамоцтвы GeoNetwork.

ЛАГІРАВАННЕ ГЭТАЙ ІНФАРМАЦЫІ, ВЕРАГОДНА, З'ЯЎЛЯЕЦЦА РЫЗЫКАЙ ДЛЯ БЯСПЕКІ І ПЕРСАНАЛЬНАЙ ІНФАРМАЦЫІ. НЕ ЎКЛЮЧАЙЦЕ ГЭТА Ў СІСТЭМЕ, ЯКАЯ ВЫКАРЫСТОЎВАЕЦЦА Ў РЭАЛЬНАСЦІ.

Мы стараемся не лагіраваць вельмі канфідэнцыйную інфармацыю - мы не лагіруем поўны токен доступу або id (толькі частку claims). Мы лагіруем аднаразовы КОД, але ён ужо павінен быць дэактываваны серверам, перш чым мы яго залагіруем.

Токен доступу, userinfo і токен id утрымліваюць канфідэнцыйную інфармацыю (напрыклад, сапраўдныя імёны, адрасы электроннай пошты і г.д...)

### Канфігурацыя для сервера Keycloak

Поўнае апісанне крокаў па наладцы keycloak выходзіць за рамкі гэтага дакумента, але гэта павінна паслужыць кіраўніцтвам.

Гэта наладзіць keycloak, які падтрымліваецца **іншым OpenID IDP** (напрыклад, Azure AD). У keycloak:

1. Стварыце realm (напрыклад, `lm`)
2. Стварыце кліент openid (напрыклад, `nt`). Гэта ваш ClientID.
    1. Root URL: ``http://localhost:7777/geonetwork`` (гэта каранёвы URL GN)
    2. Valid Redirect URIs: ``http://localhost:7777/geonetwork/*``
    3. Access Type: Confidential
    4. На ўкладцы `ls` атрымайце сакрэт (гэта ваш Client Secret)
    5. На ўкладцы `es` стварыце некалькі роляў: Administrator, Editor, Reviewer, RegisteredGuest
3. Стварыце падтрымліваючага пастаўшчыка пасведчанняў (напрыклад, да іншага сервера OpenID). Або вы можаце наладзіць карыстальнікаў непасрэдна ў keycloak.
    1. У ніжняй частцы старонкі выберыце "import from URL" і імпартуйце размяшчэнне канфігурацыі падтрымліваючага сервера.
    2. Дадайце Client Secret (з падтрымліваючага сэрвісу)
    3. Дадайце Client ID (з падтрымліваючага сэрвісу)
    4. усталюйце "Client Authentication" на "Client secret sent as post"
4. Наладзьце пераклад роляў
    1. Адрэдагуйце "Identity Provider", які вы толькі што стварылі, і перайдзіце на ўкладку "Mappers".
    2. Націсніце "Create" і дадайце "Claim to Role".
    3. Усталюйце Sync Mode Override на "Force"
    4. Claim: `es`
    5. Claim Value: `DP`
    6. Role: выберыце ролю "Administrator" з кліента `nt`.
    7. Паўтарыце вышэйапісанае для Administrator, Editor, Reviewer і RegisteredGuest
5. Наладзьце дэталі для вашага падтрымліваючага IDP
    1. Адрэдагуйце "Identity Provider", які вы толькі што наладзілі
    2. На ўкладцы Mappers, "Add Builtin" і адзначце "client roles (User Client Role)", затым "Add selected"
    3. Адрэдагуйце мапер "client roles" і пераканайцеся, што "Add to ID token" і "Add to userinfo" ўключаны

У вас павінны быць Client id Keycloak ("myclient") і сакрэт кліента. JSON канфігурацыі даступны па адрасе `https://YOUR_KEYCLOAK_HOST/realms/{YOUR REALM NAME}/.well-known/openid-configuration`

Вашы зменныя асяроддзя будуць выглядаць так:

```properties
GEONETWORK_SECURITY_TYPE=openidconnect
OPENIDCONNECT_CLIENTSECRET='...'
OPENIDCONNECT_CLIENTID='...'
OPENIDCONNECT_SERVERMETADATA_JSON_TEXT='...big json text...'
OPENIDCONNECT_IDTOKENROLELOCATION='resource_access.{your client id}.roles'
```

### Канфігурацыя Azure AD

Існуе два спосабы наладкі Azure AD. Першы - з карыстальнікамі і групамі (больш традыцыйны метад LDAP) або з ролямі прыкладання.

#### З карыстальнікамі і групамі

Наладка прыкладання Azure:

1. Стварыце новае `on`
2. выкарыстоўвайце `http://localhost:8080/geonetwork/login/oauth2/code/geonetwork-oicd` у якасці URI перанакіравання
3. На ўкладцы "Certificates & Secrets" дадайце новы сакрэт і запішыце яго (пераканайцеся, што вы атрымалі значэнне сакрэту, а НЕ id аб'екта)
4. Пераканайцеся, што групы знаходзяцца ў токене ID - на ўкладцы "Manifest" адрэдагуйце JSON так, каб было ўстаноўлена "groupMembershipClaims": "SecurityGroup"
5. На старонцы зводкі атрымайце Application (client) ID
6. На старонцы зводкі выберыце "Endpoints" (уверсе) і атрымайце тэкст JSON з "OpenID Connect metadata document" Endpoints

Наладка карыстальнікаў і груп:

1. У Azure AD перайдзіце ў групы
2. Дадайце новыя групы - "geonetworkAdmin", "geonetworkReviewer" і г.д. Запішыце імя і **Object ID** групы
3. Адрэдагуйце карыстальніка, выберыце групы і дадайце яго ў адпаведную групу.

Вашы зменныя асяроддзя будуць выглядаць так:

```properties
GEONETWORK_SECURITY_TYPE=openidconnect
OPENIDCONNECT_CLIENTSECRET='...'
OPENIDCONNECT_CLIENTID='...'
OPENIDCONNECT_SERVERMETADATA_JSON_TEXT='...big json text...'
OPENIDCONNECT_IDTOKENROLELOCATION='groups'
OPENIDCONNECT_ROLECONVERTER='3a94275f-7d53-4205-8d78-11f39e9ffa5a=Administrator,d93c6444-feee-4b67-8c0f-15d6796370cb=Reviewer'
```

!!! note

    Ролі знаходзяцца ў частцы "roles" токена ID.

!!! note

    OPENIDCONNECT_ROLECONVERTER пераўтварае Object ID групы Azure AD у ролю Geonetwork.

#### З ролямі прыкладання

Наладка прыкладання Azure:

1. Стварыце новае Enterprise application
2. выкарыстоўвайце `http://localhost:8080/geonetwork/login/oauth2/code/geonetwork-oicd` у якасці URI перанакіравання
3. На ўкладцы "Certificates & Secrets" дадайце новы сакрэт і запішыце яго (пераканайцеся, што вы атрымалі значэнне сакрэту, а НЕ id аб'екта)
4. Пераканайцеся, што групы знаходзяцца ў токене ID - на ўкладцы "Manifest" адрэдагуйце JSON так, каб было ўстаноўлена "groupMembershipClaims": "ApplicationGroup"
5. На старонцы зводкі атрымайце Application (client) ID
6. На старонцы зводкі выберыце "Endpoints" (уверсе) і атрымайце тэкст JSON з "OpenID Connect metadata document" Endpoints

Наладка роляў прыкладання:

1. У прыкладанні, якое вы стварылі, перайдзіце ў "App Roles".
2. Дадайце новыя групы - "Editor", "Reviewer" і г.д.

Прызначэнне карыстальнікаў:

1. Перайдзіце ў Azure AD, Enterprise Application, затым у прыкладанне, якое вы стварылі
2. Выберыце "Assign users and groups"
3. Націсніце "Add user/group" (уверсе)
4. Націсніце "None Selected" (у раздзеле Users) і выберыце некаторых карыстальнікаў
5. Націсніце "None Selected" (у раздзеле Select a Role) і выберыце некаторыя ролі
6. Наладзьце ўсіх вашых карыстальнікаў з ролямі

Вашы зменныя асяроддзя будуць выглядаць так:

```properties
GEONETWORK_SECURITY_TYPE=openidconnect
OPENIDCONNECT_CLIENTSECRET='...'
OPENIDCONNECT_CLIENTID='...'
OPENIDCONNECT_SERVERMETADATA_JSON_TEXT='...big json text...'
OPENIDCONNECT_IDTOKENROLELOCATION='roles'
```

!!! note

    Ролі знаходзяцца ў частцы "roles" токена ID.

!!! note

    Вам звычайна не трэба выконваць пераўтварэнне роляў, так як імя ролі будзе выкарыстоўвацца ў токене ID.

### OIDC Bearer Tokens {#oidc_bearer_tokens}

Bearer Tokens таксама падтрымліваюцца - вы можаце прымацаваць токен JWT Bearer да любога запыту, усталяваўшы загаловак HTTP наступным чынам:

```properties
Authorization: Bearer:  <JWT token>
```

Bearer Tokens у асноўным выкарыстоўваюцца для аўтаматызаваных (настольных або прыкладных) выклікаў API - рэальныя карыстальнікі павінны проста ўваходзіць у сістэму звычайным чынам з дапамогай OIDC.

1. Наладзьце вашу канфігурацыю OIDC (гл. [Наладка OAUTH2 OpenID Connect](authentication-mode.md#authentication-openid))
2. Наладзьце канфігурацыю токена OIDC Bearer (гл. [Канфігурацыя](authentication-mode.md#bearer_token_configuration))
3. Атрымайце токен Bearer з сервера OIDC. Гэта складаная частка, і ёсць некалькі спосабаў зрабіць гэта. Адзін з выкарыстоўваных спосабаў - праз працоўны працэс OAuth 2.0 Device Authorization Grant ("Device Flow").
4. Прымацуйце яго да загалоўкаў вашага запыту (гл. [OIDC Bearer Tokens](authentication-mode.md#oidc_bearer_tokens))
5. Рабіце абароненыя запыты да API Geonetwork

Гэта было пратэставана з Keycloak і з Azure AD. Гэта павінна працаваць з іншымі сэрвісамі OIDC на аснове JWT.

#### Валідацыя

Токен правяраецца трыма асноўнымі спосабамі:

1. Токен bearer будзе выкарыстоўвацца для доступу да канцавой кропкі `fo` ("валідацыя токена"), указанай у канфігурацыі OIDC. Гэта азначае, што IDP правярае токен (як мінімум яго подпіс і тэрмін дзеяння).
2. Токен bearer (JWT) будзе правераны на тое, што аўдыторыя для яго супадае з нашай наладжанай канфігурацыяй OIDC. Гэта гарантуе, што нехта не атрымлівае токен ад іншага сэрвісу і не спрабуе выкарыстоўваць яго тут. Гл. ``AudienceAccessTokenValidator.java``
3. Токен bearer (JWT) будзе правераны на тое, што суб'ект JWT і `fo` (вернуты ад IDP) супадаюць. Гэта не павінна быць праблемай у нашым выпадку выкарыстання, але спецыфікацыя OAUTH2 рэкамендуе гэтую праверку. Гл. ``SubjectAccessTokenValidator.java``

#### Канфігурацыя {#bearer_token_configuration}

Наладзьце OIDC, як паказана вышэй - пераканайцеся, што гэта працуе.

Замест выкарыстання `GEONETWORK_SECURITY_TYPE=openidconnect`, выкарыстоўвайце `GEONETWORK_SECURITY_TYPE=openidconnectbearer`.

Унутры `WEB-INF/config-security/config-security-openidconnectbearer.xml`:

1. Калі вы выкарыстоўваеце keycloak (наладжаны з групамі ў адказе `fo`), то раскаментуйце бін `er` і закаментуйце бін `er`.
2. Калі вы выкарыстоўваеце Azure AD (MS Graph API для груп карыстальніка), то раскаментуйце бін `er` і закаментуйце бін `er`.

Самы просты спосаб праверыць - атрымаць токен Bearer, а затым выкарыстоўваць плагін браўзера для дадання загалоўка ``Authorization: Bearer <token>`` да ўсіх запытаў. Калі вы наведваеце вэб-сайт Geonetwork, вы павінны ўбачыць, што ўвайшлі ў сістэму з адпаведнымі дазволамі.

#### Іншыя правайдэры

Гэта было пратэставана з Azure AD (групы ў MS Graph API) і KeyCloak (групы ў `fo`).

Для іншых IDP вам можа спатрэбіцца ўнесці некаторыя змены.

1. Пераканайцеся, што `or` і `or` працуюць правільна для вашых токенаў JWT bearer.
2. Пераканайцеся, што групы карыстальніка даступныя - гл. інтэрфейс `er` і дзве яго рэалізацыі - `er` і `er`.

## Наладка Keycloak {#authentication-keycloak}

[Keycloak](https://keycloak.org) — гэта праграмнае рашэнне для палягчэння захоўвання даных аўтэнтыфікацыі, федэрацыі карыстальнікаў, брокерыджа пасведчанняў і сацыяльнага ўваходу. GeoNetwork можна наладзіць для выкарыстання экзэмпляра keycloak для аўтэнтыфікацыі.

Усталюйце keycloak па яго інструкцыях або выкарыстоўвайце гэты прыклад наладкі ў docker <https://www.keycloak.org/getting-started/getting-started-docker>

Даныя Keycloak вызначаюцца праз зменныя асяроддзя

```text
KEYCLOAK_AUTH_SERVER_URL={keycloak url}
KEYCLOAK_REALM={realm name}
KEYCLOAK_RESOURCE={client name}
KEYCLOAK_SECRET={client secret}
KEYCLOAK_DISABLE_TRUST_MANAGER={true|false}
```

Вы можаце наладзіць больш прасунутыя параметры keycloak, адрэдагаваўшы файл **`WEB-INF/config-security/keycloak.json`**

### Канфігурацыя URL кліента Geonetwork

Пераканайцеся, што пры наладцы кліента вы наладзілі дапушчальныя uri перанакіравання на вашу ўстаноўку geonetwork. г.зн. `https://localhost:8443/geonetwork/*`. Калі гэта не наладжана правільна, вы можаце атрымаць памылку, якая ўказвае, што быў прадастаўлены няправільны uri перанакіравання. Таксама, калі вы хочаце пратэставаць backchannel logout кліента, пераканайцеся, што URL адміністратара таксама ўсталяваны на ўстаноўку geonetwork.

### Прыклад наладкі карыстальніка/ролі/групы

#### Прыклад наладкі ролі

У наладах ролі вашага кліента (clients -> myclient -> roles). Дадайце наступныя ролі

```text
Administrator
RegisteredUser
Guest
sample:UserAdmin
sample:Reviewer
sample:Editor
sample:RegisteredUser
```

#### Прыклад канфігурацыі групы

1. Перайдзіце ў групы keycloak (меню злева).
2. Стварыце новую групу з імем "Administrator"
3. Адрэдагуйце групу. Перайдзіце ў Role Mappings -> Client Roles (myclient) -> выберыце ролі адміністратара і націсніце "Add selected". Любы карыстальнік, які далучыўся да групы Administrator, будзе адміністратарам geonetwork.

#### Прыклад канфігурацыі карыстальніка

1. Перайдзіце ў карыстальнікі keycloak (меню злева)
2. Дадайце або выберыце існуючага карыстальніка. Затым перайдзіце да гэтага карыстальніка.
3. Перайдзіце ў role Mappings -> Client Roles (myclient) -> выберыце даступныя ролі для прымянення і націсніце "Add selected" або перайдзіце ў Groups -> Available Groups -> Націсніце на групу Administrator, а затым націсніце "Join"

Аналагічная наладка апісана для geoserver у [дакументацыі geoserver](https://docs.geoserver.org/latest/en/user/community/keycloak/index.html).

## Наладка EU Login {#authentication-ecas}

EU Login — гэта цэнтральны механізм уваходу Еўрапейскай камісіі. Вы можаце ўключыць уваход праз гэты цэнтральны сэрвіс, калі вашы меркаваныя карыстальнікі маюць або могуць атрымаць EU Login.

Каб уключыць EU Login, наладзьце аўтэнтыфікацыю, уключыўшы `WEB-INF/config-security/config-security-ecas.xml` у `WEB-INF/config-security/config-security.xml`, раскаментаваўшы наступны радок:

```xml
<import resource="config-security-ecas.xml"/>
```

Для EU-login патрабуецца плагін ecas, які прадастаўляецца Еўрапейскім саюзам. Плагін ecas даступны праз [CITnet](https://citnet.tech.ec.europa.eu/CITnet/nexus) для розных кантэйнераў java, такіх як Tomcat і JBoss.

Для tomcat дадайце два файлы ў папку lib tomcat: ecas-tomcat-x.y.z.jar і log4j-x.y.z.jar. Унутры папкі lib скапіруйце дзве папкі з **`eulogin-tomcat-x.y.z-config.zip`**: **`org/apache/catalina/authenticator`** і **`org/apache/catalina/startup`**. Папка mbeans змяшчае файл **`mbeans-descriptors.xml`**. Папка startup змяшчае файл **`Authenticators.properties`**. Праверце, ці давярае JDK [сертыфікатам ECAS](https://webgate.ec.europa.eu/CITnet/confluence/display/IAM/Downloads-Certificates), у адваротным выпадку імпартуйце іх у сховішча ключоў JVM.

Канфігурацыя EU Login вызначана у **`WEB-INF/config-security/config-security.properties`**. Вы можаце наладзіць сваё асяроддзе, абнавіўшы папярэдні файл або вызначыўшы перавызначэнні ўласцівасцей у файле **`WEB-INF/config-security/config-security-overrides.properties`**:

```text
cas.baseURL=https://webgate.ec.europa.eu/cas
```

Перазапусціце сэрвіс і праверце механізм аўтэнтыфікацыі.

## Наладка Shibboleth {#authentication-shibboleth}

Каталог можа працаваць у абароненай федэрацыі SAML. Shibboleth павінен быць усталяваны ў Apache, як апісана [тут](https://wiki.shibboleth.net/confluence/display/SHIB2/Installation). Доступ да каталога ажыццяўляецца праз Apache. Наладзьце аўтэнтыфікацыю Shibboleth, уключыўшы `WEB-INF/config-security/config-security-shibboleth.xml` у `WEB-INF/config-security/config-security.xml`. Затым вы можаце наладзіць сваё асяроддзе ў `config-security-shibboleth-overrides.properties`.