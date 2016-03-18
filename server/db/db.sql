--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: md5table; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE md5table (
    md5 character varying(100) NOT NULL,
    isweak character varying(5) NOT NULL,
    updatetime date NOT NULL,
    weaktype character varying(50) NOT NULL,
    text character varying(100) NOT NULL
);


ALTER TABLE md5table OWNER TO postgres;

--
-- Name: sha1table; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE sha1table (
    sha1 character varying(100) NOT NULL,
    isweak character varying(10) NOT NULL,
    updatetime date NOT NULL,
    weaktype character varying(50) NOT NULL,
    text character varying(100) NOT NULL
);


ALTER TABLE sha1table OWNER TO postgres;

--
-- Data for Name: md5table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY md5table (md5, isweak, updatetime, weaktype, text) FROM stdin;
751d31ss6b56b26b29dac2c0e1839e34	n	2016-03-18		
c20ad4d74fe97759aa27a0c99bff6710	n	2016-03-18		
e53a0a2978c28872a4505bdb51db06dc	y	2016-03-18	topN	1232
115f89503138416a242f40fb7d7f338e	y	2016-03-18	topN	223
1c63129ae9db9c60c3e8aa94d3e00495	y	2016-03-18	topN	1qaz2wsx
b9b164ad40d9ffa9c1c3b24e439424d6	y	2016-03-18	topN	q445sfd
76a2173be6393254e72ffa4d6df1030a	y	2016-03-18	topN	passwd
e53a0a2978c28872a4505bdb51db06dc	y	2016-03-18	topN	1232
115f89503138416a242f40fb7d7f338e	y	2016-03-18	topN	223
1c63129ae9db9c60c3e8aa94d3e00495	y	2016-03-18	topN	1qaz2wsx
b9b164ad40d9ffa9c1c3b24e439424d6	y	2016-03-18	topN	q445sfd
76a2173be6393254e72ffa4d6df1030a	y	2016-03-18	topN	passwd
a87ff679a2f3e71d9181a67b7542122c	y	2016-03-18	length less then 8	4
c81e728d9d4c2f636f067f89cc14862c	y	2016-03-18	length less then 8	2
cfcd208495d565ef66e7dff9f98764da	y	2016-03-18	length less then 8	0
c4ca4238a0b923820dcc509a6f75849b	y	2016-03-18	length less then 8	1
eccbc87e4b5ce2fe28308fd9f2a7baf3	y	2016-03-18	length less then 8	3
45c48cce2e2d7fbdea1afc51c7c6ad26	y	2016-03-18	length less then 8	9
c9f0f895fb98ab9159f51fd0297e236d	y	2016-03-18	length less then 8	8
1679091c5a880faf6fb5e6087eb1b2dc	y	2016-03-18	length less then 8	6
e4da3b7fbbce2345d7772b0674a318d5	y	2016-03-18	length less then 8	5
8f14e45fceea167a5a36dedd4bea2543	y	2016-03-18	length less then 8	7
e45ee7ce7e88149af8dd32b27f9512ce	y	2016-03-18	length less then 8	03
b4b147bc522828731f1a016bfa72c073	y	2016-03-18	length less then 8	00
96a3be3cf272e017046d1b2674a52bd3	y	2016-03-18	length less then 8	01
a2ef406e2c2351e0b9e80029c909242d	y	2016-03-18	length less then 8	02
7d0665438e81d8eceb98c1e31fca80c1	y	2016-03-18	length less then 8	04
faeac4e1eef307c2ab7b0a3821e6c667	y	2016-03-18	length less then 8	06
751d31dd6b56b26b29dac2c0e1839e34	y	2016-03-18	length less then 8	05
fad6f4e614a212e80c67249a666d2b09	y	2016-03-18	length less then 8	08
0a8005f5594bd67041f88c6196192646	y	2016-03-18	length less then 8	09
d72d187df41e10ea7d9fcdc7f5909205	y	2016-03-18	length less then 8	07
d3d9446802a44259755d38e6d163e820	y	2016-03-18	length less then 8	10
c51ce410c124a10e0db5e4b97fc2af39	y	2016-03-18	length less then 8	13
aab3238922bcc25a6f606eb525ffdc56	y	2016-03-18	length less then 8	14
6512bd43d9caa6e02c990b0a82652dca	n	2016-03-18		
c20ad4d76fe97759aa27a0c99bff6710	n	2016-03-18		
9bf31c7ff062936a96d3c8bd1f8f2ff3	y	2016-03-18	length less then 8	15
70efdf2ec9b086079795c442636b55fb	y	2016-03-18	length less then 8	17
c74d97b01eae257e44aa9d5bade97baf	y	2016-03-18	length less then 8	16
\.


--
-- Data for Name: sha1table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY sha1table (sha1, isweak, updatetime, weaktype, text) FROM stdin;
fb96549631c835e3339cd614cc6b5cb7d295121a	n	2016-03-18		
bcac9d1d8eab2213ae489224d0130c9468e7a0e3	n	2016-03-18		
d6a9450dc08555d6ecfaf7162e5267f401e6dd9a	y	2016-03-18	topN	1232
af06318c33c8e41c70083ee23dbe19426f1f9c5b	y	2016-03-18	topN	223
c6922b6ba9e0939583f973bc1682493351ad4fe8	y	2016-03-18	topN	1qaz2wsx
e480efc7e6029e7ade1c8da1158114623f1fc22c	y	2016-03-18	topN	q445sfd
30274c47903bd1bac7633bbf09743149ebab805f	y	2016-03-18	topN	passwd
d6a9450dc08555d6ecfaf7162e5267f401e6dd9a	y	2016-03-18	topN	1232
af06318c33c8e41c70083ee23dbe19426f1f9c5b	y	2016-03-18	topN	223
c6922b6ba9e0939583f973bc1682493351ad4fe8	y	2016-03-18	topN	1qaz2wsx
e480efc7e6029e7ade1c8da1158114623f1fc22c	y	2016-03-18	topN	q445sfd
30274c47903bd1bac7633bbf09743149ebab805f	y	2016-03-18	topN	passwd
fb96549631c835eb239cd614cc6b5cb7d295121a	y	2016-03-18	length less then 8	00
bcac9d1d8eab3713ae489224d0130c9468e7a0e3	y	2016-03-18	length less then 8	02
28a5c2818590ee3c4d5d93a448190f3397144303	y	2016-03-18	length less then 8	05
39f193cfd7d0955cc821f3074a82b7d4b89d22bc	y	2016-03-18	length less then 8	07
1ea51bf32497d1b3708522b430b288a129f65307	y	2016-03-18	length less then 8	08
4b581cdce6283495fd4934ce574ac47e92881c64	y	2016-03-18	length less then 8	09
7316b3d5fef9b3562d32f7c39f154a3bc3ab9c58	y	2016-03-18	length less then 8	06
bd307a3ec329e10a2cff8fb87480823da114f8f4	y	2016-03-18	length less then 8	13
7b52009b64fd0a2a49e6d8a939753077792b0554	y	2016-03-18	length less then 8	12
17ba0791499db908433b80f37c5fbc89b870084b	y	2016-03-18	length less then 8	11
fa35e192121eabf3dabf9f5ea6abdbcbc107ac3b	y	2016-03-18	length less then 8	14
b1d5781111d84f7b3fe45a0852e59758cd7a87e5	y	2016-03-18	length less then 8	10
f1abd670358e036c31296e66b3b66c382ac00812	y	2016-03-18	length less then 8	15
1574bddb75c78a6fd2251d61e2993b5146201319	y	2016-03-18	length less then 8	16
9e6a55b6b4563e652a23be9d623ca5055c356940	y	2016-03-18	length less then 8	18
0716d9708d321ffb6a00818614779e779925365c	y	2016-03-18	length less then 8	17
b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f	y	2016-03-18	length less then 8	19
da4b9237bacccdf19c0760cab7aec4a8359010b0	y	2016-03-18	length less then 8	2
356a192b7913b04c54574d18c28d46e6395428ab	y	2016-03-18	length less then 8	1
77de68daecd823babbb58edb1c8e14d7106e83bb	y	2016-03-18	length less then 8	3
b6589fc6ab0dc82cf12099d1c2d40ab994e8410c	y	2016-03-18	length less then 8	0
1b6453892473a467d07372d45eb05abc2031647a	y	2016-03-18	length less then 8	4
0ade7c2cf97f75d009975f4d720d1fa6c19f4897	y	2016-03-18	length less then 8	9
c1dfd96eea8cc2b62785275bca38ac261256e278	y	2016-03-18	length less then 8	6
902ba3cda1883801594b6e1b452790cc53948fda	y	2016-03-18	length less then 8	7
ac3478d69a3c81fa62e60f5c3696165a4e5e6ac4	y	2016-03-18	length less then 8	5
fe5dbbcea5ce7e2988b8c69bcfdfde8904aabc1f	y	2016-03-18	length less then 8	8
798f861ee74f6ff83ccbc9c53b419941d0080e50	y	2016-03-18	length less then 8	04
ddfe163345d338193ac2bdc183f8e9dcff904b43	y	2016-03-18	length less then 8	01
3ea6c91e241f256e5e3a88ebd647372022323a53	y	2016-03-18	length less then 8	03
\.


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

