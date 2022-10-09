from django.db import models

class Master(models.Model):
    # Login Models
    primary_key = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)

    # Organization details models
    status_choices = (('1', 'Not-Started'),
                      ('2', 'In-Progress'),
                      ('3', 'Waiting For Approval'),
                      ('4', 'Approved'))
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    manager = models.CharField(max_length=30)
    status = models.CharField(max_length=30, choices=status_choices)
    date = models.DateField()

    # DPIA Screening models
    CHOICES = (
        ('', 'Select'),
        ('', 'Not Applicable'),
        ('0', 'Yes'),
        ('1', 'No'),
    )
    DATA_PROCESS_CHOICES = (('', 'Select'),
                            ('', 'Not Applicable'),
                            ('1', 'Personal Data'),
                            ('2', 'Sensitive Personal Data'),
                            ('3', 'Both Personal and Sensitive Personal Data'),
                            ('4', 'Public Data'))
    PROCESSING_DATA_CHOICES = (('1', 'Self Processing / Data Controller'),
                               ('2', 'Data Processor'))
    name_of_organization = models.CharField(max_length=30, null=True)
    industry = models.CharField(max_length=30, null=True)
    scope_of_service_project = models.CharField(max_length=30, null=True)
    data_protection_officer = models.CharField(max_length=30, choices=CHOICES, null=True)
    name_of_DPO = models.CharField(max_length=30, null=True)
    title_of_DPO = models.CharField(max_length=30, null=True)
    data_processing_project = models.CharField(max_length=30, choices=CHOICES, null=True)
    select_data_process = models.CharField(max_length=30, choices=DATA_PROCESS_CHOICES, null=True)
    processing_data = models.CharField(max_length=30, choices=PROCESSING_DATA_CHOICES, null=True)
    data_processing_involve = models.CharField(max_length=30, choices=CHOICES)
    automated_decision_making = models.CharField(max_length=30, choices=CHOICES)
    systematic_monitoring = models.CharField(max_length=30, choices=CHOICES)
    process_data_on_large_scale = models.CharField(max_length=30, choices=CHOICES)
    data_processing_involve_reusing_old_dataset = models.CharField(max_length=30, choices=CHOICES)
    vulnerable_data_subjects = models.CharField(max_length=30, choices=CHOICES)
    data_processing_involve_innovative_technologies = models.CharField(max_length=30, choices=CHOICES)
    data_processing_involve_sharing_data_outside_european_union = models.CharField(max_length=30, choices=CHOICES)
    data_processing_involve_collection_personal_information = models.CharField(max_length=30, choices=CHOICES)
    data_processing_involve_third_party = models.CharField(max_length=30, choices=CHOICES)
    data_processing_involve_change_information_is_stored_secured = models.CharField(max_length=30, choices=CHOICES)
    data_procc_involve_chg_personal_data_currently_collected = models.CharField(max_length=30, choices=CHOICES)
    conducted_DPIA_for_similar_scope_of_service = models.CharField(max_length=30, choices=CHOICES)

    # DPIA Assessment models
    ASSESSMENT_CHOICES = (('', 'Select'),
                          ('', 'Not Applicable'),
                          ('1', 'Initial'),
                          ('2', 'Define'),
                          ('3', 'Optimized'),
                          ('4', 'Managed'))

    ASSESSMENT_CHOICES2 = (('', 'Select'),
                           ('', 'Not Applicable'),
                           ('1', 'No Process'),
                          ('2', 'Recommended'),
                          ('3', 'Important'),
                          ('4', 'Essentials'))

    ASSESSMENT_CHOICES3 = (('', 'Select'),
                           ('', 'Not Applicable'),
                           ('1', 'Absent'),
                           ('2', 'Basic'),
                           ('3', 'Intermediate'),
                           ('4', 'Advanced'))

    ASSESSMENT_CHOICES4 = (('', 'Select'),
                           ('', 'Not Applicable'),
                           ('1', 'Consent'),
                           ('Performance of contract', 'Performance of contract'),
                           ('Legitimate interest', 'Legitimate interest'),
                           ('Vital interest', 'Vital interest'),
                           ('Legal requirement', 'Legal requirement'),
                           ('Public interest', 'Public interest'))

    ASSESSMENT_RANGE_CHOICES = (('', 'Select'),
                                ('', 'Not Applicable'),
                                ('1', 'Less Than 100'),
                                ('2', '100-1000'),
                                ('3', '1000-10000'),
                                ('4', '10000-100000'),
                                ('5', 'Above 100000'))

    DATA_STORED_CHOICES = (('', 'Select'),
                           ('', 'Not Applicable'),
                           ('1', 'Shared Drive File'),
                                ('2', 'National Database'),
                                ('3', 'Paper Files'),
                                ('4', 'Cloud Storage'),
                                ('5', 'Data Center'))

    # Form 1
    f1_1 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f1_2 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f1_3 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f1_4 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f1_5 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f1_6 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)

    # Form 2
    f2_1 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES, null=True)
    f2_2 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES, null=True)
    f2_3 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f2_4 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES, null=True)
    f2_5 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f2_6 = models.CharField(max_length=30, choices=ASSESSMENT_RANGE_CHOICES, null=True)
    f2_7 = models.CharField(max_length=30, choices=DATA_STORED_CHOICES, null=True)
    f2_8 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f2_9 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES, null=True)

    # Form 3
    f3_1 = models.CharField(max_length=30, null=True)
    f3_2 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f3_3 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES2, null=True)
    f3_4 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES2, null=True)
    f3_5 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES2, null=True)
    f3_6 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES2, null=True)
    f3_7 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f3_8 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f3_9 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f3_10 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f3_11 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f3_12 = models.CharField(max_length=30,  null=True)

    # Form 4
    f4_1 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES4, null=True)
    f4_2 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES2, null=True)
    f4_3 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f4_4 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f4_5 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f4_6 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f4_7 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f4_8 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f4_9 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f4_10 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f4_11 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f4_12 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f4_13 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)

    # Form 5
    f5_1 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f5_2 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES2, null=True)
    f5_3 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES2, null=True)
    f5_4 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES2, null=True)
    f5_5 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES2, null=True)

    # Form 6
    f6_1 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f6_2 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f6_3 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f6_4 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f6_5 = models.CharField(max_length=30, choices=CHOICES, null=True)

    # Form 7
    f7_1 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f7_2 = models.CharField(max_length=30,  null=True)

    # Form 8
    f8_1 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f8_2 = models.CharField(max_length=30, choices=CHOICES, null=True)
    f8_3 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)
    f8_4 = models.CharField(max_length=30, choices=ASSESSMENT_CHOICES3, null=True)


