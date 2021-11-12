from . import get_current_lotto_numbers
HTML = """
<div class="lotto_wrap"> <div class="lotto_tit"> <a nocr="" href="?sm=tab_drt&amp;where=nexearch&amp;query=987%ED%9A%8C%EB%A1%9C%EB%98%90" class="prev _lotto-btn-prev" data-value="987">이전회차 당첨번호</a> <h3> <a nocr="" href="#" class="_lotto-btn-current"><em>988회</em>차 당첨번호 <span>2021.11.06</span></a> </h3> <div class="slc_ly _lotto-select" style="display:none"> <h4>회차별 당첨번호</h4> </div> <a nocr="" href="#" class="next off _lotto-btn-next" data-value="989">다음회차 당첨번호</a> </div> <div class="num_box"> <span class="num ball2">2</span> <span class="num ball13">13</span> <span class="num ball20">20</span> <span class="num ball30">30</span> <span class="num ball31">31</span> <span class="num ball41">41</span> <span class="bonus">보너스번호</span> <span class="num ball27">27</span> <a nocr="" onclick="return goOtherCR(this, 'a=nco_x5e*1.contents&amp;r=1&amp;i=0011AD9E_0000017BBF9A&amp;u=' + urlencode(this.href));" target="_blank" class="btn_num" href="https://www.dhlottery.co.kr/gameResult.do?method=myWin">내 번호 당첨조회</a> </div> </div>"""

def test_get_current_lotto_numbers():
    assert get_current_lotto_numbers.check_available("로또번호 조회")

    expected_html = """988회차 당첨번호 2021.11.06
로또 번호: 2, 13, 20, 30, 31, 41
보너스 번호: 27"""
    assert get_current_lotto_numbers.make_response("", HTML) == expected_html