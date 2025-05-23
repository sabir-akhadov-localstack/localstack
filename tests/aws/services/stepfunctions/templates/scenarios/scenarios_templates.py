import os
from typing import Final

from tests.aws.services.stepfunctions.templates.template_loader import TemplateLoader

_THIS_FOLDER: Final[str] = os.path.dirname(os.path.realpath(__file__))


class ScenariosTemplate(TemplateLoader):
    CATCH_EMPTY: Final[str] = os.path.join(_THIS_FOLDER, "statemachines/catch_empty.json5")
    CATCH_STATES_RUNTIME: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/catch_states_runtime.json5"
    )
    PARALLEL_STATE: Final[str] = os.path.join(_THIS_FOLDER, "statemachines/parallel_state.json5")
    PARALLEL_STATE_PARAMETERS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/parallel_state_parameters.json5"
    )
    MAX_CONCURRENCY: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/max_concurrency_path.json5"
    )
    PARALLEL_STATE_FAIL: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/parallel_state_fail.json5"
    )
    PARALLEL_NESTED_NESTED: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/parallel_state_nested.json5"
    )
    PARALLEL_STATE_CATCH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/parallel_state_catch.json5"
    )
    PARALLEL_STATE_RETRY: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/parallel_state_retry.json5"
    )
    PARALLEL_STATE_ORDER: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/parallel_state_order.json5"
    )
    PARALLEL_STATE_SERVICE_LAMBDA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/parallel_state_service_lambda.json5"
    )
    MAP_STATE: Final[str] = os.path.join(_THIS_FOLDER, "statemachines/map_state.json5")
    MAP_STATE_LEGACY: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_legacy.json5"
    )
    MAP_STATE_LEGACY_CONFIG_INLINE: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_legacy_config_inline.json5"
    )
    MAP_STATE_LEGACY_CONFIG_DISTRIBUTED: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_legacy_config_distributed.json5"
    )
    MAP_STATE_LEGACY_CONFIG_DISTRIBUTED_PARAMETERS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_legacy_config_distributed_parameters.json5"
    )
    MAP_STATE_LEGACY_CONFIG_DISTRIBUTED_ITEM_SELECTOR: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_legacy_config_distributed_item_selector.json5"
    )
    MAP_STATE_LEGACY_CONFIG_INLINE_PARAMETERS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_legacy_config_inline_parameters.json5"
    )
    MAP_STATE_LEGACY_CONFIG_INLINE_ITEM_SELECTOR: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_legacy_config_inline_item_selector.json5"
    )
    MAP_STATE_CONFIG_DISTRIBUTED_PARAMETERS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_config_distributed_parameters.json5"
    )
    MAP_STATE_CONFIG_DISTRIBUTED_ITEM_SELECTOR: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_config_distributed_item_selector.json5"
    )
    MAP_STATE_CONFIG_DISTRIBUTED_ITEMS_PATH_FROM_PREVIOUS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_config_distributed_items_path_from_previous.json5"
    )
    MAP_STATE_CONFIG_DISTRIBUTED_ITEM_SELECTOR_PARAMETERS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_config_distributed_item_selector_parameters.json5"
    )
    MAP_STATE_LEGACY_REENTRANT: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_legacy_reentrant.json5"
    )
    MAP_STATE_CONFIG_DISTRIBUTED_REENTRANT: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_config_distributed_reentrant.json5"
    )
    MAP_STATE_CONFIG_DISTRIBUTED_REENTRANT_LAMBDA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_config_distributed_reentrant_lambda.json5"
    )
    MAP_STATE_CONFIG_INLINE_PARAMETERS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_config_inline_parameters.json5"
    )
    MAP_STATE_CONFIG_INLINE_ITEM_SELECTOR: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_config_inline_item_selector.json5"
    )
    MAP_STATE_NESTED: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_nested.json5"
    )
    MAP_STATE_NESTED_CONFIG_DISTRIBUTED: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_nested_config_distributed.json5"
    )
    MAP_STATE_NESTED_CONFIG_DISTRIBUTED_NO_MAX_CONCURRENCY: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_nested_config_distributed_no_max_concurrency.json5"
    )
    MAP_STATE_NO_PROCESSOR_CONFIG: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_no_processor_config.json5"
    )
    MAP_ITEM_READER_BASE_LIST_OBJECTS_V2: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_item_reader_base_list_objects_v2.json5"
    )
    MAP_ITEM_READER_BASE_CSV_HEADERS_FIRST_LINE: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_item_reader_base_csv_headers_first_line.json5"
    )
    MAP_ITEM_READER_BASE_CSV_MAX_ITEMS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_item_reader_base_csv_max_items.json5"
    )
    MAP_ITEM_READER_BASE_CSV_MAX_ITEMS_PATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_item_reader_base_csv_max_items_path.json5"
    )
    MAP_ITEM_READER_BASE_CSV_HEADERS_DECL: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_item_reader_base_csv_headers_decl.json5"
    )
    MAP_ITEM_READER_BASE_JSON: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_item_reader_base_json.json5"
    )
    MAP_ITEM_READER_BASE_JSON_MAX_ITEMS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_item_reader_base_json_max_items.json5"
    )
    MAP_ITEM_READER_BASE_JSON_MAX_ITEMS_JSONATA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_item_reader_base_json_max_items_jsonata.json5"
    )
    MAP_ITEM_READER_BASE_JSON_WITH_ITEMS_PATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_item_reader_base_json_with_items_path.json5"
    )
    MAP_ITEM_BATCHER_BASE_JSON_MAX_PER_BATCH_JSONATA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_item_batcher_base_max_per_batch_jsonata.json5"
    )
    MAP_STATE_ITEM_SELECTOR: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_item_selector.json5"
    )
    MAP_STATE_ITEM_SELECTOR_JSONATA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_item_selector_jsonata.json5"
    )
    MAP_STATE_ITEM_SELECTOR_PARAMETERS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_item_selector_parameters.json5"
    )
    MAP_STATE_ITEMS: Final[str] = os.path.join(_THIS_FOLDER, "statemachines/map_state_items.json5")
    MAP_STATE_ITEMS_VARIABLE: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_items_variable.json5"
    )
    MAP_STATE_ITEMS_LITERAL: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_items_literal.json5"
    )
    MAP_STATE_PARAMETERS_LEGACY: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_parameters_legacy.json5"
    )
    MAP_STATE_ITEM_SELECTOR_SINGLETON: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_item_selector_singletons.json5"
    )
    MAP_STATE_PARAMETERS_SINGLETON_LEGACY: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_parameters_singletons_legacy.json5"
    )
    MAP_STATE_CATCH: Final[str] = os.path.join(_THIS_FOLDER, "statemachines/map_state_catch.json5")
    MAP_STATE_CATCH_EMPTY_FAIL: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_catch_empty_fail.json5"
    )
    MAP_STATE_CATCH_LEGACY: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_catch_legacy.json5"
    )
    MAP_STATE_LEGACY_REENTRANT: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_legacy_reentrant.json5"
    )
    MAP_STATE_RETRY: Final[str] = os.path.join(_THIS_FOLDER, "statemachines/map_state_retry.json5")
    MAP_STATE_RETRY_LEGACY: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_retry_legacy.json5"
    )
    MAP_STATE_RETRY_MULTIPLE_RETRIERS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_retry_multiple_retriers.json5"
    )
    MAP_STATE_BREAK_CONDITION: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_break_condition.json5"
    )
    MAP_STATE_BREAK_CONDITION_LEGACY: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_break_condition_legacy.json5"
    )
    MAP_STATE_TOLERATED_FAILURE_COUNT: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_tolerated_failure_count.json5"
    )
    MAP_STATE_TOLERATED_FAILURE_COUNT_PATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_tolerated_failure_count_path.json5"
    )
    MAP_STATE_TOLERATED_FAILURE_PERCENTAGE: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_tolerated_failure_percentage.json5"
    )
    MAP_STATE_TOLERATED_FAILURE_PERCENTAGE_PATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_tolerated_failure_percentage_path.json5"
    )
    MAP_STATE_LABEL: Final[str] = os.path.join(_THIS_FOLDER, "statemachines/map_state_label.json5")
    MAP_STATE_LABEL_EMPTY_FAIL: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_label_empty_fail.json5"
    )
    MAP_STATE_LABEL_INVALID_CHAR_FAIL: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_label_invalid_char_fail.json5"
    )
    MAP_STATE_LABEL_TOO_LONG_FAIL: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_label_too_long_fail.json5"
    )
    MAP_STATE_RESULT_WRITER: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/map_state_result_writer.json5"
    )
    CHOICE_STATE_UNSORTED_CHOICE_PARAMETERS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/choice_state_unsorted_choice_parameters.json5"
    )
    CHOICE_CONDITION_CONSTANT_JSONATA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/choice_state_condition_constant_jsonata.json5"
    )
    CHOICE_STATE_UNSORTED_CHOICE_PARAMETERS_JSONATA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/choice_state_unsorted_choice_parameters_jsonata.json5"
    )
    CHOICE_STATE_SINGLETON_COMPOSITE: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/choice_state_singleton_composite.json5"
    )
    CHOICE_STATE_SINGLETON_COMPOSITE_JSONATA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/choice_state_singleton_composite_jsonata.json5"
    )
    CHOICE_STATE_SINGLETON_COMPOSITE_LITERAL_JSONATA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/choice_state_singleton_composite_literal_string_jsonata.json5"
    )
    CHOICE_STATE_AWS_SCENARIO: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/choice_state_aws_scenario.json5"
    )
    CHOICE_STATE_AWS_SCENARIO_JSONATA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/choice_state_aws_scenario_jsonata.json5"
    )
    LAMBDA_EMPTY_RETRY: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/lambda_empty_retry.json5"
    )
    LAMBDA_INVOKE_WITH_RETRY_BASE: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/lambda_invoke_with_retry_base.json5"
    )
    LAMBDA_INVOKE_WITH_RETRY_BASE_EXTENDED_INPUT: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/lambda_invoke_with_retry_extended_input.json5"
    )
    LAMBDA_SERVICE_INVOKE_WITH_RETRY_BASE_EXTENDED_INPUT: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/lambda_service_invoke_with_retry_extended_input.json5"
    )
    RETRY_INTERVAL_FEATURES: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/retry_interval_features.json5"
    )
    RETRY_INTERVAL_FEATURES_JITTER_NONE: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/retry_interval_features_jitter_none.json5"
    )
    RETRY_INTERVAL_FEATURES_MAX_ATTEMPTS_ZERO: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/retry_interval_features_max_attempts_zero.json5"
    )
    WAIT_TIMESTAMP: Final[str] = os.path.join(_THIS_FOLDER, "statemachines/wait_timestamp.json5")
    WAIT_TIMESTAMP_PATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/wait_timestamp_path.json5"
    )
    WAIT_TIMESTAMP_JSONATA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/wait_timestamp_jsonata.json5"
    )
    WAIT_SECONDS_JSONATA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/wait_seconds_jsonata.json5"
    )
    DIRECT_ACCESS_CONTEXT_OBJECT_CHILD_FIELD: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/direct_access_context_object_child_field.json5"
    )

    RAISE_FAILURE_ERROR_JSONATA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/fail_error_jsonata.json5"
    )
    RAISE_FAILURE_CAUSE_JSONATA: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/fail_cause_jsonata.json5"
    )

    INVALID_JSONPATH_IN_ERRORPATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/invalid_jsonpath_in_errorpath.json5"
    )
    INVALID_JSONPATH_IN_CAUSEPATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/invalid_jsonpath_in_causepath.json5"
    )
    INVALID_JSONPATH_IN_STRING_EXPR_JSONPATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/invalid_jsonpath_in_string_expr_jsonpath.json5"
    )
    INVALID_JSONPATH_IN_STRING_EXPR_CONTEXTPATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/invalid_jsonpath_in_string_expr_contextpath.json5"
    )
    INVALID_JSONPATH_IN_HEARTBEATSECONDSPATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/invalid_jsonpath_in_heartbeatsecondspath.json5"
    )
    INVALID_JSONPATH_IN_TIMEOUTSECONDSPATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/invalid_jsonpath_in_timeoutsecondspath.json5"
    )
    INVALID_JSONPATH_IN_INPUTPATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/invalid_jsonpath_in_inputpath.json5"
    )
    INVALID_JSONPATH_IN_OUTPUTPATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/invalid_jsonpath_in_outputpath.json5"
    )
    ESCAPE_SEQUENCES_STRING_LITERALS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/escape_sequences_string_literals.json5"
    )
    ESCAPE_SEQUENCES_JSONPATH: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/escape_sequences_jsonpath.json5"
    )
    ESCAPE_SEQUENCES_JSONATA_COMPARISON_OUTPUT: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/escape_sequences_jsonata_comparison_output.json5"
    )
    ESCAPE_SEQUENCES_JSONATA_COMPARISON_ASSIGN: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/escape_sequences_jsonata_comparison_assign.json5"
    )
    ESCAPE_SEQUENCES_ILLEGAL_INTRINSIC_FUNCTION: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/escape_sequences_illegal_intrinsic_function.json5"
    )
    ESCAPE_SEQUENCES_ILLEGAL_INTRINSIC_FUNCTION_2: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/escape_sequences_illegal_intrinsic_function_2.json5"
    )
