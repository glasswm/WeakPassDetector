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
    weaktype integer NOT NULL,
    text character varying(100)
);


ALTER TABLE md5table OWNER TO postgres;

--
-- Name: sha1table; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE sha1table (
    sha1 character varying(100) NOT NULL,
    isweak character varying(10) NOT NULL,
    updatetime date NOT NULL,
    weaktype integer NOT NULL,
    text character varying(100)
);


ALTER TABLE sha1table OWNER TO postgres;

--
-- Data for Name: md5table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY md5table (md5, isweak, updatetime, weaktype, text) FROM stdin;
\.


--
-- Data for Name: sha1table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY sha1table (sha1, isweak, updatetime, weaktype, text) FROM stdin;
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

