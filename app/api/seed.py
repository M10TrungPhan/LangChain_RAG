'''
seed.py users the models in model.py and populates the database with dummy content
'''

# ----------------
# Database imports
# ----------------
from helpers import (
    create_org_by_org_or_uuid,
    create_project_by_org,
    create_document_by_file_path,
    get_org_by_uuid_or_namespace
)
from config import (
    FILE_UPLOAD_PATH,
    logger
)
from util import (
    get_file_hash
)
import os

# --------------------
# Create organizations
# --------------------

organizations = [
    {
    'display_name': 'Knowledge Handbooks',
    'namespace': 'knowledge handbooks',
    'projects': [
        {
            'display_name': 'Bón phân',
            'docs': [
                'knowledge_handbooks_Bón_đạm_cho_lúa_vào_thời_kỳ_nào_là_tốt_nhất.md',
                'knowledge_handbooks_Cách_bón_lót_cho_cà_phê_trồng_mới.md',
                'knowledge_handbooks_Cách_bón_phân_chuồng_cho_rau_màu_hiệu_quả_nhất.md',
                'knowledge_handbooks_Có_cần_bón_phân_hữu_cơ_cho_đất_phèn_không.md',
                'knowledge_handbooks_Bón_vôi_đúng_quy_trình_cho_vườn_cây_ăn_trái.md'           
            ]
        },
        {
            'display_name': 'Phòng trị sâu bệnh',
            'docs': [                
                'knowledge_handbooks_Cam_sành_ra_bông__bị_mưa_nhiều_cần_làm_gì.md',
                'knowledge_handbooks_Cách_chăm_sóc_lúa_giai_đoạn_đòng_trổ_giúp_tăng_năng_suất_hiệu_quả.md',
                'knowledge_handbooks_Cách_khắc_phục_bưởi_da_xanh_bị_vàng_đọt.md',
                'knowledge_handbooks_Cách_khắc_phục_hiện_tượng_nứt_trái_trên_cây_trồng.md',
                'knowledge_handbooks_Cách_khắc_phục_mít_xơ_đen.md',
                'knowledge_handbooks_Cách_phòng_trị_sâu_vẽ_bùa_trên_cây_cam.md',
                'knowledge_handbooks_Cách_phòng_trừ_bệnh_khô_cành_khô_quả_gây_hại_cây_cà_phê.md',
                'knowledge_handbooks_Cách_trị_sâu_vẽ_bùa_trên_bưởi.md'
            ]
        },
        {
            'display_name': 'Kỹ thuật nông nghiệp',
            'docs': [
                'knowledge_handbooks_3_bước_cải_tạo_đất_sau_thu_hoạch_đối_với_vườn_cây_ăn_trái.md',
                'knowledge_handbooks_Cây_cà_phê_già_cỗi_thì_phải_làm_thế_nào.md',
                'knowledge_handbooks_Cách_làm_cho_hoa_cà_phê_ra_đồng_loạt.md',
                'knowledge_handbooks_Cách_tưới_nước_cho_mô_hình_trồng_hồ_tiêu_xen_cà_phê.md',
                'knowledge_handbooks_Cần_làm_gì_sau_khi_thu_hoạch_sầu_riêng.md',
                'knowledge_handbooks_Dứt_điểm_rệp_sáp__rầy_trắng_ở_phần_rễ.md',
                'knowledge_handbooks_Giữ_ẩm_cho_đất_trong_mùa_khô_như_thế_nào.md',
                'knowledge_handbooks_Giống_cà_phê_vối_nào_chất_lượng_tốt_nhất_hiện_nay.md',
                'knowledge_handbooks_Kinh_nghiệm_chăm_sóc_sầu_riêng_giai_đoạn_nuôi_trái_non_hiệu_quả.md',
                'knowledge_handbooks_Kích_thước_phẳng_của_bầu_ươm_cà_phê_ra_sao.md',
                'knowledge_handbooks_Kỹ_thuật_cắt_tỉa_cành_và_tạo_tán_cho_cà_phê.md'
            ]
        }],

},
    {
    'display_name': 'Category Trees',
    'namespace': 'category trees',
    'projects': [
        {
            'display_name': 'Cây ăn quả',
            'docs': [
                'category_trees_Dừa.md',
                'category_trees_Dừa_nước__dừa_lá.md',
                'category_trees_Chuối_rẽ_quạt.md',
                'category_trees_Sầu_riêng.md',
                'category_trees_Mía.md'

            ]
        },
        {
            'display_name': 'Cây nông nghiệp, công nghiệp',
            'docs': [                
                'category_trees_Cà_phê.md',
                'category_trees_Hồ_tiêu.md',
                'category_trees_Lúa.md'
            ]
        },
        {
            'display_name': 'Cây hoa',
            'docs': [    
                'category_trees_Lô_hội__nha_đam.md',            
                'category_trees_Hoa_ly.md',
                'category_trees_Lan_Cattleya.md',
                'category_trees_Lan_Chi.md',
                'category_trees_Lan_chu_đính.md',
                'category_trees_Lan_dạ_hương.md',
                'category_trees_Lan_Vanda.md',
                'category_trees_Lay_ơn.md',
                'category_trees_Lẻ_bạn__sò_huyết__bang_hoa.md',
                'category_trees_Sen_đá.md'
            ]
        },
        {
            'display_name': 'Cây cảnh',
            'docs': [
                'category_trees_Lục_bình.md',
                'category_trees_Phong_Lộc_Hoa.md',
                'category_trees_Thiên_tuế.md',
                'category_trees_Thốt_nốt.md',
                'category_trees_Thủy_trúc__lác_dù.md',
                'category_trees_Thủy_tùng.md',
                'category_trees_Tre_mạnh_tông.md',
                'category_trees_Trắc_bá_diệp.md',
                'category_trees_Vạn_tuế.md',
                'category_trees_Đại_tướng_quân.md',
                'category_trees_Đủng_đỉnh.md',
                'category_trees_Cau.md',
                'category_trees_Cau_bẹ_đỏ__Cau_kiểng_đỏ.md',
                'category_trees_Cau_bụng__Cau_Vua.md',
                'category_trees_Cau_kiểng_vàng__Cau_đuôi_phượng.md',
                'category_trees_Cau_tiểu_trâm.md',
                'category_trees_Cọ_cảnh.md',
                'category_trees_Cọ_dầu__dừa_dầu.md'
            ]
        },
        {
            'display_name': 'Rau củ quả',
            'docs': [
                'category_trees_Củ_năng__mã_thầy.md',
                'category_trees_Gừng.md',
                'category_trees_Sả.md',
                'category_trees_Huỳnh_tinh.md',
                'category_trees_Khoai_ngọt__khoai_mỡ.md',
                'category_trees_Khoai_từ.md',
                'category_trees_Kim_châm__hoa_hiên__huyên_thảo.md',
                'category_trees_Kê.md',
                'category_trees_Măng_tây.md',
                'category_trees_Rau_hoa_chuối.md',
                'category_trees_Nghệ.md',
                'category_trees_Nấm_linh_chi.md',
                'category_trees_Sâm_đại_hành__tỏi_Lào__hành_Lào.md'

            ]
        }]

}
]

training_data_path = os.path.join(os.path.dirname(__file__), f'{FILE_UPLOAD_PATH}/training_data')

for org in organizations:
    try:
        org_obj = create_org_by_org_or_uuid(
            display_name=org['display_name'],
            namespace=org['namespace']
        )
    except:
        org_obj = get_org_by_uuid_or_namespace(org['namespace'],  should_except=False)
    logger.debug(f'🏠  Created organization: {org_obj.display_name}')

    if 'projects' not in org:
        continue

    for project in org['projects']:
        project['organization'] = org_obj

        project_obj = create_project_by_org(
            organization_id=org_obj,
            display_name=project['display_name']
        )
        logger.debug(f'🗂️  Created project: {project_obj.display_name}')

        project_uuid = str(project_obj.uuid)
        org_uuid = str(org_obj.uuid)

        # if the directory does not exist, create it
        if not os.path.exists(os.path.join(FILE_UPLOAD_PATH, org_uuid, project_uuid)):
            os.mkdir(os.path.join(FILE_UPLOAD_PATH, org_uuid, project_uuid))

        if 'docs' not in project:
            continue

        for doc in project['docs']:
            file_path = os.path.join(training_data_path, doc)

            # check if file exists
            if os.path.isfile(file_path):
                file_hash = get_file_hash(file_path)
                # try:
                create_document_by_file_path(
                    organization=org_obj,
                    project=project_obj,
                    file_path=file_path,
                    file_hash=file_hash
                )
                # except:
                #      logger.info(f'  ❌  Created document: {doc}')
                logger.info(f'  ✅  Created document: {doc}')

            else:
                logger.error(f' ❌  Document not found: {doc}')