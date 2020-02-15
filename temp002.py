#encoding:utf-8
cities = ['武汉', '孝感', '黄冈', '荆州', '随州', '襄阳', '鄂州', '宜昌', '黄石', '荆门', '咸宁', '十堰', '仙桃', '天门', '恩施州', '潜江', '神农架林区', '深圳', '广州', '东莞', '珠海', '佛山', '惠州', '中山', '江门', '汕头', '湛江', '茂名', '肇庆', '梅州', '阳江', '韶关', '清远', '揭阳', '汕尾', '潮州', '河源', '待明确地区', '信阳', '南阳', '郑州', '驻马店', '商丘', '周口', '新乡', '平顶山', '安阳', '许昌', '漯河', '洛阳', '焦作', '开封', '濮阳', '鹤壁', '济源', '三门峡', '待明确地区', '温州', '宁波', '杭州', '台州', '嘉兴', '金华', '绍兴', '衢州', '丽水', '湖州', '舟山', '蚌埠', '合肥', '阜阳', '亳州', '六安', '安庆', '宿州', '马鞍山', '芜湖', '淮北', '铜陵', '淮南', '池州', '黄山', '滁州', '宣城', '南昌', '上饶', '九江', '新余', '宜春', '赣州', '抚州', '萍乡', '鹰潭', '吉安', '景德镇', '赣江新区', '长沙', '岳阳', '株洲', '常德', '邵阳', '娄底', '益阳', '衡阳', '湘潭', '永州', '郴州', '怀化', '湘西自治州', '张家界', '南京', '苏州', '徐州', '淮安', '无锡', '连云港', '常州', '南通', '泰州', '盐城', '扬州', '镇江', '宿迁', '青岛', '济南', '潍坊', '济宁', '烟台', '聊城', '威海', '德州', '泰安', '淄博', '临沂', '枣庄', '日照', '菏泽', '滨州', '万州区', '江北区', '綦江区', '合川区', '九龙坡区', '垫江县', '奉节县', '渝中区', '潼南区', '两江新区', '南岸区', '大足区', '云阳县', '忠县', '长寿区', '渝北区', '石柱县', '荣昌区', '丰都县', '铜梁区', '沙坪坝区', '开州区', '巫溪县', '巫山县', '巴南区', '璧山区', '大渡口区', '永川区', '高新区', '江津区', '梁平区', '涪陵区', '彭水县', '武隆区', '酉阳县', '万盛经开区', '黔江区', '城口县', '秀山县', '哈尔滨', '双鸭山', '鸡西', '绥化', '齐齐哈尔', '大庆', '七台河', '黑河', '牡丹江', '佳木斯', '鹤岗', '大兴安岭', '伊春', '成都', '甘孜州', '达州', '南充', '巴中', '广安', '绵阳', '内江', '泸州', '德阳', '凉山州', '自贡', '遂宁', '眉山', '宜宾', '雅安', '广元', '攀枝花', '乐山', '资阳', '阿坝州', '朝阳区', '海淀区', '西城区', '大兴区', '丰台区', '外地来京人员', '昌平区', '通州区', '房山区', '石景山区', '东城区', '顺义区', '怀柔区', '密云区', '门头沟区', '延庆区', '待明确地区', '福州', '莆田', '泉州', '厦门', '宁德', '漳州', '南平', '三明', '龙岩', '待明确地区', '外地来沪人员', '浦东新区', '宝山区', '徐汇区', '闵行区', '松江区', '静安区', '长宁区', '普陀区', '杨浦区', '嘉定区', '奉贤区', '虹口区', '黄浦区', '崇明区', '青浦区', '金山区', '唐山', '沧州', '张家口', '邯郸', '石家庄', '廊坊', '保定', '邢台', '秦皇岛', '衡水', '承德', '南宁', '北海', '桂林', '河池', '柳州', '防城港', '来宾', '玉林', '钦州', '贵港', '贺州', '百色', '梧州', '待明确地区', '西安', '汉中', '安康', '渭南', '咸阳', '宝鸡', '商洛', '铜川', '延安', '榆林', '韩城', '杨凌', '待明确地区', '昆明', '昭通', '西双版纳', '玉溪', '保山', '曲靖', '大理州', '红河州', '普洱', '德宏州', '楚雄州', '丽江', '文山州', '临沧', '待明确地区', '三亚', '海口', '儋州', '万宁', '澄迈', '昌江', '琼海', '陵水', '临高', '保亭', '文昌', '东方', '乐东', '定安', '琼中', '贵阳', '遵义', '毕节', '黔南州', '六盘水', '黔东南州', '铜仁', '安顺', '黔西南州', '沈阳', '大连', '盘锦', '葫芦岛', '阜新', '锦州', '铁岭', '朝阳', '鞍山', '丹东', '本溪', '辽阳', '营口', '晋中', '太原', '运城', '大同', '长治', '忻州', '晋城', '朔州', '阳泉', '吕梁', '临汾', '宝坻区', '河东区', '河北区', '北辰区', '南开区', '外地来津人员', '和平区', '宁河区', '东丽区', '滨海新区', '河西区', '西青区', '武清区', '津南区', '红桥区', '乌鲁木齐', '伊犁州', '兵团第四师', '兵团第九师', '昌吉州', '巴州', '兵团第八师石河子市', '兵团第六师五家渠市', '吐鲁番市', '兵团第十二师', '兵团第七师', '阿克苏地区', '长春', '四平市', '辽源', '公主岭', '延边', '通化', '吉林市', '松原', '白城', '梅河口', '包头', '鄂尔多斯', '巴彦淖尔', '呼和浩特', '通辽', '赤峰', '呼伦贝尔', '锡林郭勒盟', '乌兰察布', '乌海市', '兴安盟', '兰州', '平凉', '甘南', '天水', '定西', '白银', '陇南', '庆阳', '临夏', '张掖', '金昌', '待明确地区', '吴忠', '银川', '固原', '中卫', '宁东', '石嘴山', '西宁', '海北州', '拉萨']
def cityNums():
    i = 0
    for city in cities:
        print(city, i)
        i += 1

confirms = ['确诊', '54406', '37914', '3114', '2817', '1478', '1232', '1128', '1192', '906', '980', '902', '840', '597', '514', '422', '244', '116', '10', '1294', '406', '335', '81', '95', '84', '58', '65', '22', '25', '22', '13', '17', '15', '13', '10', '12', '8', '5', '5', '3', '0', '1212', '252', '150', '144', '138', '90', '70', '55', '58', '51', '37', '34', '31', '30', '25', '17', '19', '4', '7', '0', '1162', '499', '154', '166', '145', '43', '55', '42', '21', '17', '10', '10', '950', '153', '168', '150', '107', '63', '82', '39', '35', '31', '26', '28', '23', '17', '9', '13', '6', '913', '222', '123', '115', '127', '102', '76', '72', '32', '18', '20', '5', '1', '1001', '241', '153', '78', '78', '100', '75', '59', '47', '35', '43', '39', '40', '8', '5', '604', '91', '86', '77', '60', '52', '46', '43', '40', '37', '27', '21', '12', '12', '530', '56', '47', '42', '49', '46', '38', '38', '36', '32', '28', '47', '24', '15', '18', '14', '537', '104', '26', '22', '23', '20', '20', '20', '20', '17', '17', '15', '14', '23', '19', '18', '15', '14', '9', '10', '9', '8', '20', '13', '10', '6', '8', '7', '5', '4', '4', '4', '3', '2', '1', '1', '1', '2', '2', '1', '425', '167', '48', '45', '46', '36', '19', '16', '13', '12', '15', '5', '2', '1', '470', '139', '44', '36', '35', '24', '30', '22', '22', '19', '17', '11', '9', '10', '8', '11', '7', '6', '13', '3', '3', '1', '375', '59', '58', '46', '39', '38', '26', '24', '17', '14', '14', '12', '10', '7', '7', '3', '1', '0', '285', '66', '55', '46', '34', '25', '20', '20', '13', '6', '0', '326', '109', '56', '20', '18', '18', '14', '16', '13', '11', '9', '9', '9', '7', '6', '3', '5', '3', '0', '291', '46', '46', '33', '31', '27', '29', '32', '22', '10', '8', '7', '235', '49', '43', '31', '22', '24', '17', '11', '10', '8', '8', '4', '3', '5', '0', '232', '114', '21', '24', '15', '17', '13', '7', '8', '8', '3', '1', '1', '0', '168', '48', '25', '15', '14', '13', '13', '9', '8', '4', '5', '4', '7', '2', '1', '162', '54', '33', '15', '13', '9', '7', '6', '4', '6', '3', '3', '3', '2', '3', '1', '143', '34', '31', '23', '17', '10', '10', '10', '4', '4', '119', '28', '18', '11', '11', '8', '12', '7', '6', '4', '7', '3', '3', '1', '127', '35', '19', '19', '12', '8', '7', '8', '7', '4', '6', '2', '121', '47', '14', '12', '6', '6', '6', '6', '4', '4', '3', '4', '4', '2', '1', '2', '70', '23', '16', '10', '4', '4', '3', '3', '2', '2', '1', '1', '1', '88', '44', '14', '7', '6', '5', '3', '5', '2', '1', '1', '68', '11', '11', '8', '7', '6', '7', '6', '6', '3', '2', '1', '56', '90', '35', '9', '8', '12', '9', '4', '4', '3', '3', '2', '1', '0', '70', '27', '33', '5', '3', '1', '1', '18', '10', '18', '15', '3', '1', '1', '确诊', '259', '67', '33', '28', '19', '16', '16', '15', '15', '11', '9', '8', '8', '3', '3', '3', '2', '2', '1', '1', '1', '1', '1', '1', '253', '67', '33', '28', '19', '16', '16', '15', '15', '11', '9', '8', '7', '3', '3', '3', '2', '2', '1', '1', '1', '1', '1', '251', '58', '33', '28', '19', '16', '16', '15', '14', '11', '9', '8', '7', '3', '3', '3', '2', '2', '1', '1', '1', '1', '1', '203', '50', '33', '28', '18', '16', '15', '15', '13', '11', '8', '8', '7', '3', '3', '3', '2', '2', '1', '1', '1', '1', '1', '161', '47', '33', '28', '18', '15', '15', '14', '13', '11', '8', '8', '7', '3', '3', '3', '2', '2', '1', '1', '1', '1', '1', '156', '45', '32', '27', '18', '15', '14', '14', '12', '11', '8', '7', '7', '3', '3', '3', '2', '2', '1', '1', '1', '1', '1', '95', '40', '32', '27', '17', '15', '14', '14', '12', '11', '7', '7', '3', '3', '3', '3', '2', '2', '1', '1', '1', '1', '1', '89', '33', '32', '24', '16', '15', '13', '13', '12', '11', '7', '5', '3', '3', '3', '3', '2', '1', '1', '1', '1', '1', '1', '86', '33', '25', '24', '15', '15']

def confirmNums():
    i = 0
    for confirm in confirms:
        print("confirm: ", i)
        i+= 1

if __name__ == '__main__':
    confirmNums()