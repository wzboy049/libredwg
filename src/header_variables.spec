/* -*- c -*- */
/*****************************************************************************/
/*  LibreDWG - free implementation of the DWG file format                    */
/*                                                                           */
/*  Copyright (C) 2010 Free Software Foundation, Inc.                        */
/*                                                                           */
/*  This library is free software, licensed under the terms of the GNU       */
/*  General Public License as published by the Free Software Foundation,     */
/*  either version 3 of the License, or (at your option) any later version.  */
/*  You should have received a copy of the GNU General Public License        */
/*  along with this program.  If not, see <http://www.gnu.org/licenses/>.    */
/*****************************************************************************/

/*
 * header_variables.spec: DWG header variables specification
 * written by Felipe Corrêa da Silva Sances
 * modified by Anderson Cardoso
 * modified by Reini Urban
 */

#include "spec.h"

  VERSION(R_2007)
    {
      FIELD_RL(bitsize);
    }
  SINCE(R_2013)
    {
      FIELD_BLL(requiredversions);
    }

  SINCE(R_13)
    {
      FIELD_BD (unknown_0); // max double number? 412148564080.0
      FIELD_BD (unknown_1); // default extrusion.x? 1.0
      FIELD_BD (unknown_2); // default extrusion.y? 1.0
      FIELD_BD (unknown_3); // default extrusion.z? 1.0
    }
  VERSIONS(R_13, R_2007) { // undocumented as such in the ODA spec
      FIELD_TV (unknown_text1); // ""
      FIELD_TV (unknown_text2); // ""
      FIELD_TV (unknown_text3); // ""
      FIELD_TV (unknown_text4); // ""
  }
  SINCE(R_13)
    {
      FIELD_BL (unknown_8); // 24
      FIELD_BL (unknown_9); // 0
    }
  VERSIONS(R_13, R_14) // or maybe UNTIL(R_14)
    {
      FIELD_BS(unknown_10);
    }
  VERSIONS(R_13, R_2000)
    {
      FIELD_HANDLE (current_viewport_entity_header, ANYCODE);
    }
  SINCE(R_13)
    {
      FIELD_B (DIMASO);
      FIELD_B (DIMSHO);
    }
  VERSIONS(R_13, R_14)
    {
      FIELD_B (DIMSAV); // Name of the dimensioning style?
    }
  SINCE(R_13)
    {
      FIELD_B (PLINEGEN);
      FIELD_B (ORTHOMODE);
      FIELD_B (REGENMODE);
      FIELD_B (FILLMODE);
      FIELD_B (QTEXTMODE);
      FIELD_B (PSLTSCALE);
      FIELD_B (LIMCHECK);
    }
  VERSIONS(R_13, R_14)
    {
      FIELD_B (BLIPMODE);
    }

  SINCE(R_2004)
    {
      FIELD_B (unknown_11); //undocumented
    }

  FIELD_B (user_timer_onoff);
  FIELD_B (SKPOLY);
  FIELD_B (ANGDIR);
  FIELD_B (SPLFRAME);

  VERSIONS(R_13, R_14)
    {
      IF_ENCODE_FROM_EARLIER {
         FIELD_VALUE(ATTREQ) = 1;
         FIELD_VALUE(ATTREQ) = 1;
         FIELD_VALUE(HANDLING) = 1;
      }
      FIELD_B (ATTREQ);
      FIELD_B (ATTDIA);
    }

  FIELD_B (MIRRTEXT);
  FIELD_B (WORLDVIEW); // default: 1

  VERSIONS(R_13, R_14)
    {
      FIELD_B (WIREFRAME); //Undocumented
    }

  FIELD_B (TILEMODE);  // default: 1
  FIELD_B (PLIMCHECK);
  FIELD_B (VISRETAIN); // default: 1

  VERSIONS(R_13, R_14)
    {
      FIELD_B (DELOBJ);
    }

  FIELD_B (DISPSILH);
  FIELD_B (PELLIPSE);

  VERSION(R_13)
    {
      FIELD_BS (SAVEIMAGES);
    }

  VERSIONS(R_14, R_2000)
    {
      IF_ENCODE_FROM_EARLIER {
         FIELD_VALUE(PROXYGRAPHICS) = 1;
      }
      FIELD_BS (PROXYGRAPHICS);
    }

  VERSIONS(R_13, R_14)
    {
      IF_ENCODE_FROM_EARLIER {
         FIELD_VALUE(DRAGMODE) = 2;
      }
      FIELD_BS (DRAGMODE);
    }

  SINCE(R_13)
    {
      IF_ENCODE_FROM_EARLIER {
         FIELD_VALUE(TREEDEPTH) = 3020;
      }
      FIELD_BS (TREEDEPTH);
    }
  FIELD_BS (LUNITS);
  FIELD_BS (LUPREC);
  FIELD_BS (AUNITS);
  FIELD_BS (AUPREC);

  VERSIONS(R_13, R_14)
    {
      FIELD_BS (OSMODE);
    }

  FIELD_BS (ATTMODE);

  VERSIONS(R_13, R_14)
    {
      FIELD_BS (COORDS);
    }

  FIELD_BS (PDMODE);

  VERSIONS(R_13, R_14)
    {
      FIELD_BS (PICKSTYLE);
    }

  SINCE(R_2004)
    {
      FIELD_BL (unknown_12);
      FIELD_BL (unknown_13);
      FIELD_BL (unknown_14);
      FIELD_BL (unknown_14b);
    }

  FIELD_BS (USERI1);
  FIELD_BS (USERI2);
  FIELD_BS (USERI3);
  FIELD_BS (USERI4);
  FIELD_BS (USERI5);
  FIELD_BS (SPLINESEGS);
  FIELD_BS (SURFU);
  FIELD_BS (SURFV);
  FIELD_BS (SURFTYPE);
  FIELD_BS (SURFTAB1);
  FIELD_BS (SURFTAB2);
  FIELD_BS (SPLINETYPE);
  FIELD_BS (SHADEDGE); // default: 3
  FIELD_BS (SHADEDIF); // default: 70
  FIELD_BS (UNITMODE);
  FIELD_BS (MAXACTVP); // default: 64
  FIELD_BS (ISOLINES);
  FIELD_BS (CMLJUST);
  FIELD_BS (TEXTQLTY);
  FIELD_BD (LTSCALE);
  FIELD_BD (TEXTSIZE);
  FIELD_BD (TRACEWID);
  FIELD_BD (SKETCHINC);
  FIELD_BD (FILLETRAD);
  FIELD_BD (THICKNESS);
  FIELD_BD (ANGBASE);
  FIELD_BD (PDSIZE);
  FIELD_BD (PLINEWID);
  FIELD_BD (USERR1);
  FIELD_BD (USERR2);
  FIELD_BD (USERR3);
  FIELD_BD (USERR4);
  FIELD_BD (USERR5);
  FIELD_BD (CHAMFERA);
  FIELD_BD (CHAMFERB);
  FIELD_BD (CHAMFERC);
  FIELD_BD (CHAMFERD);
  FIELD_BD (FACETRES);
  FIELD_BD (CMLSCALE);
  FIELD_BD (CELTSCALE);
  FIELD_TV (MENU);
  FIELD_BL (TDCREATE_JULIAN_DAY);
  FIELD_BL (TDCREATE_MILLISECONDS);
  FIELD_BL (TDUPDATE_JULIAN_DAY);
  FIELD_BL (TDUPDATE_MILLISECONDS);

  SINCE(R_2004)
    {
      FIELD_BL (unknown_15);
      FIELD_BL (unknown_16);
      FIELD_BL (unknown_17);
    }

  FIELD_BL (TDINDWG_DAYS);
  FIELD_BL (TDINDWG_MILLISECONDS);
  FIELD_BL (TDUSRTIMER_DAYS);
  FIELD_BL (TDUSRTIMER_MILLISECONDS);
  FIELD_CMC (CECOLOR);
  FIELD_HANDLE (HANDSEED, ANYCODE);
  FIELD_HANDLE (CLAYER, ANYCODE);
  FIELD_HANDLE (TEXTSTYLE, ANYCODE);
  FIELD_HANDLE (CELTYPE, ANYCODE);

  SINCE(R_2007)
    {
      FIELD_HANDLE (CMATERIAL, ANYCODE);
    }

  FIELD_HANDLE (DIMSTYLE, ANYCODE);
  FIELD_HANDLE (CMLSTYLE, ANYCODE);

  SINCE(R_2000)
    {
      FIELD_BD (PSVPSCALE);
    }

  SINCE(R_13)
    {
      FIELD_3BD (PINSBASE);
      FIELD_3BD (PEXTMIN);
      FIELD_3BD (PEXTMAX);
      FIELD_2RD (PLIMMIN);
      FIELD_2RD (PLIMMAX);
      FIELD_BD (PELEVATION);
      FIELD_3BD (PUCSORG);
      FIELD_3BD (PUCSXDIR);
      FIELD_3BD (PUCSYDIR);
      FIELD_HANDLE (PUCSNAME, ANYCODE);
    }

  SINCE(R_2000)
    {
      FIELD_HANDLE (PUCSBASE, ANYCODE);
      FIELD_BS (PUCSORTHOVIEW);
      FIELD_HANDLE (PUCSORTHOREF, ANYCODE);
      FIELD_3BD (PUCSORGTOP);
      FIELD_3BD (PUCSORGBOTTOM);
      FIELD_3BD (PUCSORGLEFT);
      FIELD_3BD (PUCSORGRIGHT);
      FIELD_3BD (PUCSORGFRONT);
      FIELD_3BD (PUCSORGBACK);
    }

  FIELD_3BD (INSBASE);
  FIELD_3BD (EXTMIN);
  FIELD_3BD (EXTMAX);
  FIELD_2RD (LIMMIN);
  FIELD_2RD (LIMMAX);
  FIELD_BD (ELEVATION);
  FIELD_3BD (UCSORG);
  FIELD_3BD (UCSXDIR);
  FIELD_3BD (UCSYDIR);
  FIELD_HANDLE (UCSNAME, ANYCODE);

  SINCE(R_2000)
    {
      FIELD_HANDLE (UCSBASE, ANYCODE);
      FIELD_BS (UCSORTHOVIEW);
      FIELD_HANDLE (UCSORTHOREF, ANYCODE);
      FIELD_3BD (UCSORGTOP);
      FIELD_3BD (UCSORGBOTTOM);
      FIELD_3BD (UCSORGLEFT);
      FIELD_3BD (UCSORGRIGHT);
      FIELD_3BD (UCSORGFRONT);
      FIELD_3BD (UCSORGBACK);
      FIELD_TV (DIMPOST);
      FIELD_TV (DIMAPOST);
    }

  VERSIONS(R_13, R_14)
    {
      FIELD_B (DIMTOL);
      FIELD_B (DIMLIM);
      FIELD_B (DIMTIH);
      FIELD_B (DIMTOH);
      FIELD_B (DIMSE1);
      FIELD_B (DIMSE2);
      FIELD_B (DIMALT);
      FIELD_B (DIMTOFL);
      FIELD_B (DIMSAH);
      FIELD_B (DIMTIX);
      FIELD_B (DIMSOXD);
      FIELD_CAST (DIMALTD, RC, BS);
      FIELD_CAST (DIMZIN, RC, BS);
      FIELD_B (DIMSD1);
      FIELD_B (DIMSD2);
      FIELD_CAST (DIMTOLJ, RC, BS);
      FIELD_CAST (DIMJUST, RC, BS);
      FIELD_CAST (DIMFIT, RC, BS);
      FIELD_B (DIMUPT);
      FIELD_CAST (DIMTZIN, RC, BS);
      FIELD_CAST (DIMMALTZ, RC, BS);
      FIELD_CAST (DIMMALTTZ, RC, BS);
      FIELD_CAST (DIMTAD, RC, BS);
      FIELD_BS (DIMUNIT);
      FIELD_BS (DIMAUNIT);
      FIELD_BS (DIMDEC);
      FIELD_BS (DIMTDEC);
      FIELD_BS (DIMALTU);
      FIELD_BS (DIMALTTD);
      FIELD_HANDLE (DIMTXSTY, ANYCODE);
    }

  FIELD_BD (DIMSCALE);
  FIELD_BD (DIMASZ);
  FIELD_BD (DIMEXO);
  FIELD_BD (DIMDLI);
  FIELD_BD (DIMEXE);
  FIELD_BD (DIMRND);
  FIELD_BD (DIMDLE);
  FIELD_BD (DIMMTP);
  FIELD_BD (DIMMTM);

  SINCE(R_2007)
    {
      FIELD_BD (DIMFXL);
      FIELD_BD (DIMJOGANG);
      FIELD_BS (DIMTFILL);
      FIELD_CMC (DIMTFILLCLR);
    }

  SINCE(R_2000)
    {
      FIELD_B (DIMTOL);
      FIELD_B (DIMLIM);
      FIELD_B (DIMTIH);
      FIELD_B (DIMTOH);
      FIELD_B (DIMSE1);
      FIELD_B (DIMSE2);
      FIELD_BS (DIMTAD);
      FIELD_BS (DIMZIN);
      FIELD_BS (DIMAZIN);
    }

  SINCE(R_2007)
    {
      FIELD_BS (DIMARCSYM);
    }

  FIELD_BD (DIMTXT);
  FIELD_BD (DIMCEN);
  FIELD_BD (DIMTSZ);
  FIELD_BD (DIMALTF);
  FIELD_BD (DIMLFAC);
  FIELD_BD (DIMTVP);
  FIELD_BD (DIMTFAC);
  FIELD_BD (DIMGAP);

  VERSIONS(R_13, R_14)
    {
      FIELD_T (DIMPOST_T);
      FIELD_T (DIMAPOST_T);
      FIELD_T (DIMBLK_T);
      FIELD_T (DIMBLK1_T);
      FIELD_T (DIMBLK2_T);
    }

  SINCE(R_2000)
    {
      FIELD_BD (DIMALTRND);
      FIELD_B (DIMALT);
      FIELD_BS (DIMALTD);
      FIELD_B (DIMTOFL);
      FIELD_B (DIMSAH);
      FIELD_B (DIMTIX);
      FIELD_B (DIMSOXD);
    }

  FIELD_CMC (DIMCLRD);
  FIELD_CMC (DIMCLRE);
  FIELD_CMC (DIMCLRT);

  SINCE(R_2000)
    {
      FIELD_BS (DIMADEC);
      FIELD_BS (DIMDEC);
      FIELD_BS (DIMTDEC);
      FIELD_BS (DIMALTU);
      FIELD_BS (DIMALTTD);
      FIELD_BS (DIMAUNIT);
      FIELD_BS (DIMFRAC);
      FIELD_BS (DIMLUNIT);
      FIELD_BS (DIMDSEP);
      FIELD_BS (DIMTMOVE);
      FIELD_BS (DIMJUST);
      FIELD_B (DIMSD1);
      FIELD_B (DIMSD2);
      FIELD_BS (DIMTOLJ);
      FIELD_BS (DIMTZIN);
      FIELD_BS (DIMALTZ);
      FIELD_BS (DIMALTTZ);
      FIELD_B (DIMUPT);
      FIELD_BS (DIMATFIT);
    }

  SINCE(R_2007)
    {
      FIELD_B (DIMFXLON);
    }

  SINCE(R_2010)
    {
      FIELD_B (DIMTXTDIRECTION);
      FIELD_BD (DIMALTMZF);
      FIELD_T (DIMALTMZS);
      FIELD_BD (DIMMZF);
      FIELD_T (DIMMZS);
    }

  SINCE(R_2000)
    {
      FIELD_HANDLE (DIMTXSTY, ANYCODE);
      FIELD_HANDLE (DIMLDRBLK, ANYCODE);
      FIELD_HANDLE (DIMBLK, ANYCODE);
      FIELD_HANDLE (DIMBLK1, ANYCODE);
      FIELD_HANDLE (DIMBLK2, ANYCODE);
    }

  SINCE(R_2007)
    {
      FIELD_HANDLE (DIMLTYPE, ANYCODE);
      FIELD_HANDLE (DIMLTEX1, ANYCODE);
      FIELD_HANDLE (DIMLTEX2, ANYCODE);
    }

  SINCE(R_2000)
    {
      FIELD_BS (DIMLWD);
      FIELD_BS (DIMLWE);
    }

  FIELD_HANDLE (BLOCK_CONTROL_OBJECT, ANYCODE);
  FIELD_HANDLE (LAYER_CONTROL_OBJECT, ANYCODE);
  FIELD_HANDLE (STYLE_CONTROL_OBJECT, ANYCODE);
  FIELD_HANDLE (LINETYPE_CONTROL_OBJECT, ANYCODE);
  FIELD_HANDLE (VIEW_CONTROL_OBJECT, ANYCODE);
  FIELD_HANDLE (UCS_CONTROL_OBJECT, ANYCODE);
  FIELD_HANDLE (VPORT_CONTROL_OBJECT, ANYCODE);
  FIELD_HANDLE (APPID_CONTROL_OBJECT, ANYCODE);
  FIELD_HANDLE (DIMSTYLE_CONTROL_OBJECT, ANYCODE);

  VERSIONS(R_13, R_2000)
    {
      FIELD_HANDLE (VIEWPORT_ENTITY_HEADER_CONTROL_OBJECT, ANYCODE);
    }

  FIELD_HANDLE (DICTIONARY_ACAD_GROUP, ANYCODE);
  FIELD_HANDLE (DICTIONARY_ACAD_MLINESTYLE, ANYCODE);
  FIELD_HANDLE (DICTIONARY_NAMED_OBJECTS, ANYCODE);

  SINCE(R_2000)
    {
      IF_ENCODE_FROM_EARLIER {
         FIELD_VALUE(TSTACKALIGN) = 1;
         FIELD_VALUE(TSTACKSIZE) = 70;
      }
      FIELD_BS (TSTACKALIGN);
      FIELD_BS (TSTACKSIZE);
      FIELD_TV (HYPERLINKBASE);
      FIELD_TV (STYLESHEET);
      FIELD_HANDLE (DICTIONARY_LAYOUTS, ANYCODE);
      FIELD_HANDLE (DICTIONARY_PLOTSETTINGS, ANYCODE);
      FIELD_HANDLE (DICTIONARY_PLOTSTYLES, ANYCODE);
    }

  SINCE(R_2004)
    {
      FIELD_HANDLE (DICTIONARY_MATERIALS, ANYCODE);
      FIELD_HANDLE (DICTIONARY_COLORS, ANYCODE);
    }

  SINCE(R_2007)
    {
      FIELD_HANDLE (DICTIONARY_VISUALSTYLE, ANYCODE);
    }

  SINCE(R_2013)
    {
      FIELD_HANDLE (unknown_20, ANYCODE); //  DICTIONARY_LIGHTLIST? since 2010
    }
  SINCE(R_2000)
    {
      FIELD_BL (FLAGS);
      DECODER {
          FIELD_VALUE(CELWEIGHT) = FIELD_VALUE(FLAGS) & 0x1f;
          FIELD_VALUE(ENDCAPS)   = FIELD_VALUE(FLAGS) & 0x60 ? 1 : 0;
          FIELD_VALUE(JOINSTYLE) = FIELD_VALUE(FLAGS) & 0x180 ? 1 : 0;
          FIELD_VALUE(LWDISPLAY) = FIELD_VALUE(FLAGS) & 0x200 ? 0 : 1;
          FIELD_VALUE(XEDIT)     = FIELD_VALUE(FLAGS) & 0x400 ? 0 : 1;
          FIELD_VALUE(EXTNAMES)  = FIELD_VALUE(FLAGS) & 0x800 ? 1 : 0;
          FIELD_VALUE(PSTYLEMODE) = FIELD_VALUE(FLAGS) & 0x2000 ? 1 : 0;
          FIELD_VALUE(OLESTARTUP) = FIELD_VALUE(FLAGS) & 0x4000 ? 1 : 0;
      }
      FIELD_BS (INSUNITS);
      FIELD_BS (CEPSNTYPE);
      if (FIELD_VALUE(CEPSNTYPE) == 3)
        {
          FIELD_HANDLE (CPSNID, ANYCODE);
        }
      FIELD_TV (FINGERPRINTGUID);
      FIELD_TV (VERSIONGUID);
    }

  SINCE(R_2004)
    {
      FIELD_RC (SORTENTS);
      FIELD_RC (INDEXCTL);
      FIELD_RC (HIDETEXT);
      FIELD_RC (XCLIPFRAME);
      FIELD_RC (DIMASSOC);
      FIELD_RC (HALOGAP);
      FIELD_BS (OBSCOLOR);
      FIELD_BS (INTERSECTIONCOLOR);
      FIELD_RC (OBSLTYPE);
      FIELD_RC (INTERSECTIONDISPLAY);
      FIELD_TV (PROJECTNAME);
    }

  FIELD_HANDLE (BLOCK_RECORD_PAPER_SPACE, ANYCODE);
  FIELD_HANDLE (BLOCK_RECORD_MODEL_SPACE, ANYCODE);
  FIELD_HANDLE (LTYPE_BYLAYER, ANYCODE);
  FIELD_HANDLE (LTYPE_BYBLOCK, ANYCODE);
  FIELD_HANDLE (LTYPE_CONTINUOUS, ANYCODE);

  SINCE(R_2007)
    {
      FIELD_B (CAMERADISPLAY);
      FIELD_BL (unknown_21);
      FIELD_BL (unknown_22);
      FIELD_BD (unknown_23);
      FIELD_BD (STEPSPERSEC);
      FIELD_BD (STEPSIZE);
      FIELD_BD (_3DDWFPREC);
      FIELD_BD (LENSLENGTH);
      FIELD_BD (CAMERAHEIGHT);
      FIELD_RC (SOLIDHIST);
      FIELD_RC (SHOWHIST);
      FIELD_BD (PSOLWIDTH);
      FIELD_BD (PSOLHEIGHT);
      FIELD_BD (LOFTANG1);
      FIELD_BD (LOFTANG2);
      FIELD_BD (LOFTMAG1);
      FIELD_BD (LOFTMAG2);
      FIELD_BS (LOFTPARAM);
      FIELD_RC (LOFTNORMALS);
      FIELD_BD (LATITUDE);
      FIELD_BD (LONGITUDE);
      FIELD_BD (NORTHDIRECTION);
      FIELD_BL (TIMEZONE);
      FIELD_RC (LIGHTGLYPHDISPLAY);
      FIELD_RC (TILEMODELIGHTSYNCH);
      FIELD_RC (DWFFRAME);
      FIELD_RC (DGNFRAME);
      FIELD_B (unknown_47);
      FIELD_CMC (INTERFERECOLOR);
      FIELD_HANDLE (INTERFEREOBJVS, ANYCODE);
      FIELD_HANDLE (INTERFEREVPVS, ANYCODE);
      FIELD_HANDLE (DRAGVS, ANYCODE);
      FIELD_RC (CSHADOW);
      FIELD_BD (unknown_53);
    }

  SINCE(R_14)
    {
      FIELD_BS (unknown_54); /* (type 5/6 only) these do not seem to be required */
      FIELD_BS (unknown_55);
      FIELD_BS (unknown_56);
      FIELD_BS (unknown_57);
    }

  /* TODO: This really is the section[0] CRC not related to the header */
  FIELD_RS (CRC);



