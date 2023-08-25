SET @SLNG_YMD = '20230818';

SELECT * from t_slng_schdl_cbn_cnt WHERE SLNG_YMD > @SLNG_YMD AND (preo_cnt < 0 OR mkrv_cnt < 0 OR rmn_cnt < 0 ) ORDER BY REG_DT DESC;
SELECT * from t_slng_schdl_cbn WHERE SLNG_YMD > @SLNG_YMD AND (preo_cnt < 0 OR mkrv_cnt < 0 OR rmn_cnt < 0) ORDER BY REG_DT DESC;
SELECT * from t_slng_schdl_seat WHERE SLNG_YMD > @SLNG_YMD AND (preo_cnt < 0 OR mkrv_cnt < 0 OR rmn_cnt < 0);
SELECT * from t_slng_schdl_crg WHERE SLNG_YMD > @SLNG_YMD AND (preo_cnt < 0 OR mkrv_cnt < 0 OR rmn_cnt < 0 );
SELECT * from t_slng_schdl_crg_cnt WHERE SLNG_YMD > @SLNG_YMD AND (preo_cnt < 0);
/*
UPDATE t_slng_schdl_cbn
	SET
		  RMN_CNT = RMN_CNT + PREO_CNT
		, PREO_CNT = 0
	WHERE SLNG_YMD > @SLNG_YMD
	AND preo_cnt < 0 
	AND RMN_CNT > 0;*/
SELECT * FROM t_slng_schdl_cbn_cnt
WHERE SLNG_YMD > @SLNG_YMD AND (preo_cnt < 0 OR mkrv_cnt < 0 OR rmn_cnt < 0 );
