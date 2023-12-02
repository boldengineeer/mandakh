PGDMP         4    
            {            lab8    15.4    15.4                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16398    lab8    DATABASE        CREATE DATABASE lab8 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE lab8;
                postgres    false            �            1259    16406    Category    TABLE     `   CREATE TABLE public."Category" (
    catid integer NOT NULL,
    "Catname" character varying
);
    DROP TABLE public."Category";
       public         heap    postgres    false            �            1259    16418    SubCategory    TABLE     �   CREATE TABLE public."SubCategory" (
    catid integer NOT NULL,
    subcatid integer NOT NULL,
    subcatname character varying
);
 !   DROP TABLE public."SubCategory";
       public         heap    postgres    false            �            1259    16440    User    TABLE     �   CREATE TABLE public."User" (
    userid integer NOT NULL,
    username character varying,
    password character varying,
    email character varying,
    fullname character varying
);
    DROP TABLE public."User";
       public         heap    postgres    false            �            1259    16399    news    TABLE     �   CREATE TABLE public.news (
    "news_id " integer NOT NULL,
    "Title" character varying,
    "Content" character varying,
    "Category" integer NOT NULL,
    "Subcategory" integer NOT NULL,
    userid integer NOT NULL,
    date date
);
    DROP TABLE public.news;
       public         heap    postgres    false                      0    16406    Category 
   TABLE DATA           6   COPY public."Category" (catid, "Catname") FROM stdin;
    public          postgres    false    215   �                 0    16418    SubCategory 
   TABLE DATA           D   COPY public."SubCategory" (catid, subcatid, subcatname) FROM stdin;
    public          postgres    false    216   �                 0    16440    User 
   TABLE DATA           M   COPY public."User" (userid, username, password, email, fullname) FROM stdin;
    public          postgres    false    217   5       
          0    16399    news 
   TABLE DATA           g   COPY public.news ("news_id ", "Title", "Content", "Category", "Subcategory", userid, date) FROM stdin;
    public          postgres    false    214   �       s           2606    16412    Category Category_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public."Category"
    ADD CONSTRAINT "Category_pkey" PRIMARY KEY (catid);
 D   ALTER TABLE ONLY public."Category" DROP CONSTRAINT "Category_pkey";
       public            postgres    false    215            w           2606    16446    User User_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_pkey" PRIMARY KEY (userid);
 <   ALTER TABLE ONLY public."User" DROP CONSTRAINT "User_pkey";
       public            postgres    false    217            q           2606    16405    news news_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.news
    ADD CONSTRAINT news_pkey PRIMARY KEY ("news_id ");
 8   ALTER TABLE ONLY public.news DROP CONSTRAINT news_pkey;
       public            postgres    false    214            u           2606    16424    SubCategory subcatid_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public."SubCategory"
    ADD CONSTRAINT subcatid_pkey PRIMARY KEY (subcatid);
 E   ALTER TABLE ONLY public."SubCategory" DROP CONSTRAINT subcatid_pkey;
       public            postgres    false    216            {           2606    16462 "   SubCategory SubCategory_catid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."SubCategory"
    ADD CONSTRAINT "SubCategory_catid_fkey" FOREIGN KEY (catid) REFERENCES public."Category"(catid) NOT VALID;
 P   ALTER TABLE ONLY public."SubCategory" DROP CONSTRAINT "SubCategory_catid_fkey";
       public          postgres    false    216    215    3187            x           2606    16413    news news_Category_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.news
    ADD CONSTRAINT "news_Category_fkey" FOREIGN KEY ("Category") REFERENCES public."Category"(catid) NOT VALID;
 C   ALTER TABLE ONLY public.news DROP CONSTRAINT "news_Category_fkey";
       public          postgres    false    215    214    3187            y           2606    16435    news news_Subcategory_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.news
    ADD CONSTRAINT "news_Subcategory_fkey" FOREIGN KEY ("Subcategory") REFERENCES public."SubCategory"(subcatid) NOT VALID;
 F   ALTER TABLE ONLY public.news DROP CONSTRAINT "news_Subcategory_fkey";
       public          postgres    false    3189    214    216            z           2606    16447    news news_userid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.news
    ADD CONSTRAINT news_userid_fkey FOREIGN KEY (userid) REFERENCES public."User"(userid) NOT VALID;
 ?   ALTER TABLE ONLY public.news DROP CONSTRAINT news_userid_fkey;
       public          postgres    false    217    214    3191               8   x�3漰��
�.����e�_l�����9/,���¾���b���� rD�         O   x�3�42�0����.츰�ˈ�Ȑ��, {�}\���@م6\�|�H�U�����{��f�4P�R {7�x� f0q         �   x�3��/�L��細00ᬂp�s3s���s9/L���bÅ6_l�����
�_Z��b�M��]l���b��Sjv*gRj���	�J�F6i"Д�@�Q͙xa߅�� rrFeV�rs&�&%:T&f��C��paHH��&�����^l:�5&�+F��� �Wm�      
   q   x�]α	�0���K$w�l��A��\$�Fp���L*�4���?.���7�O���mǃ��!fR� ���%8�Ff��ak8���تhU�M��DF|F���蘳5yqν1�r5     