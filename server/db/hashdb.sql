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
    md5 character varying(32),
    isweak character varying(2),
    updatetime date,
    weaktype character varying(20)
);


ALTER TABLE md5table OWNER TO postgres;

--
-- Name: sha1table; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE sha1table (
    sha1 character varying(40),
    isweak character varying(2),
    updatetime date,
    weaktype character varying(20)
);


ALTER TABLE sha1table OWNER TO postgres;

--
-- Data for Name: md5table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY md5table (md5, isweak, updatetime, weaktype) FROM stdin;
c81e728d9d4c2f636f067f89cc14862c	y	2015-11-05	u
cfcd208495d565ef66e7dff9f98764da	y	2015-11-05	u
c4ca4238a0b923820dcc509a6f75849b	y	2015-11-05	u
e4da3b7fbbce2345d7772b0674a318d5	y	2015-11-05	u
eccbc87e4b5ce2fe28308fd9f2a7baf3	y	2015-11-05	u
a87ff679a2f3e71d9181a67b7542122c	y	2015-11-05	u
1679091c5a880faf6fb5e6087eb1b2dc	y	2015-11-05	u
c9f0f895fb98ab9159f51fd0297e236d	y	2015-11-05	u
8f14e45fceea167a5a36dedd4bea2543	y	2015-11-05	u
96a3be3cf272e017046d1b2674a52bd3	y	2015-11-05	u
45c48cce2e2d7fbdea1afc51c7c6ad26	y	2015-11-05	u
b4b147bc522828731f1a016bfa72c073	y	2015-11-05	u
a2ef406e2c2351e0b9e80029c909242d	y	2015-11-05	u
e45ee7ce7e88149af8dd32b27f9512ce	y	2015-11-05	u
7d0665438e81d8eceb98c1e31fca80c1	y	2015-11-05	u
d72d187df41e10ea7d9fcdc7f5909205	y	2015-11-05	u
751d31dd6b56b26b29dac2c0e1839e34	y	2015-11-05	u
faeac4e1eef307c2ab7b0a3821e6c667	y	2015-11-05	u
fad6f4e614a212e80c67249a666d2b09	y	2015-11-05	u
d3d9446802a44259755d38e6d163e820	y	2015-11-05	u
0a8005f5594bd67041f88c6196192646	y	2015-11-05	u
c51ce410c124a10e0db5e4b97fc2af39	y	2015-11-05	u
6512bd43d9caa6e02c990b0a82652dca	y	2015-11-05	u
c20ad4d76fe97759aa27a0c99bff6710	n	2015-11-05	u
9bf31c7ff062936a96d3c8bd1f8f2ff3	y	2015-11-05	u
aab3238922bcc25a6f606eb525ffdc56	y	2015-11-05	u
c74d97b01eae257e44aa9d5bade97baf	y	2015-11-05	u
70efdf2ec9b086079795c442636b55fb	y	2015-11-05	u
\.


--
-- Data for Name: sha1table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY sha1table (sha1, isweak, updatetime, weaktype) FROM stdin;
\.


--
-- Name: un_md5; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY md5table
    ADD CONSTRAINT un_md5 UNIQUE (md5);


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

